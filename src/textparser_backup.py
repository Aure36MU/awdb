#!/usr/bin/python
# -*- coding: UTF-8 -*-

import io

from __future__ import print_function #UNIX systems : Disable default print function



####################
# GLOBAL CONSTANTS #
####################
GLOBAL_SEP = "***" #Separates objects (used between each Unit or CO)
LINE_SEP = '\n' #Separates lines (keep this)
ELEMENT_SEP = ';' #Separates elements (used between multiple commands)
COMMAND_TITLE = ':' #Separates name of command and its arguments

#######################
# CLASS : TEXT PARSER #
#######################
"""
Source content : File | List of List of String (2d String array)
int line_pointer
int word_pointer

The content is organized like this :
[ [line_1],[line_2],[line_3], ...[line_n] ]
where lines are :
["CO_name"] <- 1st line of CO in CO_balance
["Effect_name","COzone_size_and_type","command_1", ..."command_n"] <- 2nd line of CO in CO_balance
["COP_name","command_1", ..."command_n"] <- 3rd line of CO in CO_balance
["SCOP_name","command_1", ..."command_n"] <- 4th line of CO in CO_balance
["***"] <- Unit or CO separator
["Unit_name"] <- 1st line of Unit in Unit_balance
["cost","movement","movement_type","fuel+x_per_turn","vision","weapon_code"] <- 2nd line of Unit in Unit_balance
["first_weapon_name","ammo","attack_type","range"] <- if weapon_code == 1 or 3 : 3rd line of Unit in Unit_balance
["second_weapon_name","attack_type","range"] <- if weapon_code == 2 or 3 : 3rd or 4th line of Unit in Unit_balance
["command_1|property_1", ... "command_n|property_n"] <- Last line of Unit in Unit_balance

"""


class TextParser:
		#TODO rework this with better handling of lines+words (maybe define a single get and a single adv)

	def __init__(self, filename=None):
		if filename is None:
			content = []
			pass #Maybe throw an exception since dealing with something with does not come from a file may be tedious. ???
		else:
			with open(filename) as f:
				content = []
				#1) Append lines
				for line in f:
					content.append(line)
				#2) Split lines
				content = splitList(content, LINE_SEP)

				#TODO find a way to avoid creating empty elements ; or create a function
				while '' in content :
					content.remove('')
				#3) Split by elements in each line then remove exceeding whitespace
				for i,line in enumerate(content):
					content[i] = split(content[i], ELEMENT_SEP)
					content[i] = stripList(content[i])

		self.content = content
		self.line_pointer = 0
		self.word_pointer = 0
					

	""" start()

	Start the reading of the file. Relocate the two pointers at the very beginning.
	"""
	def start(self):
		self.line_pointer = 0
		self.word_pointer = 0


	""" setPointers()

	Relocate the pointers at the specified positions (line, word).
	"""
	def setPointers(self, line, word):
		self.line_pointer = line
		self.word_pointer = word


	""" getWord() -> String

	A word is defined by a series of char until a separator. Default separators are defined at the beginning of this file. Or you can specify one by yourself. ?????

	"""
	def getNextWord(self):
		try:
			res = self.content[self.line_pointer][self.word_pointer]
		except IndexError: #if (self.word_pointer >= self.content[self.line_pointer].length):
			res = self.content[self.line_pointer+1][0]
		return res


	""" advWord()

	word_pointer moves to the next word.
	Does NOT return anything. Use getWord() instead.
	"""
	def advWord(self):
		self.word_pointer = self.word_pointer + 1


	""" getLine() -> List of String

	"""
	def getLine(self):
		res = self.content[self.line_pointer]
		return res



	""" advLine()

	line_pointer moves to the next line.
	Does NOT return anything. Use getLine() instead.
	"""
	def advLine(self):
		self.line_pointer = self.line_pointer + 1
		self.word_pointer = 0


	""" getCommand()

	"""
	def getCommand(self):
		if COMMAND_TITLE in self.getWord():
			return res



	""" doCommand()

	Do a command as specified on AWBW_command_list. First argument must be the command name (else it returns CommandNameError), then a series of arguments which do not conflict with the command (else it returns CommandArgError).
	"""
	def doCommand(self):
		pass


	def display(self):
		print("Content = ", self.content, "\nLine = ", self.line_pointer, "\nWord = ", self.word_pointer)



###################
# OTHER FUNCTIONS #
###################

""" split() -> String

Equivalent to calling the prebuild split() method in String class.
"""
def split(s, char, nbsplit=-1):
	return s.split(char, nbsplit)


""" splitKeep() -> List of String

Splits a String into a list where elements are separated by occurences of specified char.
Example : splitKeep("hello_world!", ' ') -> ["hello", "_", "world!"]
The split() prebuild function would return ["hello", "world!"]
"""
def splitKeep(s, char):

	scopy = s
	parts = ("","","")
	res = []
	while (scopy.find(char) != -1):
		parts = scopy.partition(char)
		if (parts[0] != ""):
			res.append(parts[0])
		res.append(parts[1])
		scopy = parts[2]
	if (scopy != ""):
		res.append(scopy)
	
	return res



""" splitList() -> List of String

Iterates split() for each element of the parameter.
"""
def splitList(strlist, char, nbsplit=-1):
	scopy = []
	if not(isinstance(strlist, list)):
		scopy.append(strlist)
	else: 
		scopy = strlist

	res = []
	for element in range(len(scopy)):
		scurrent = scopy[element].split(char, nbsplit)

		for element2 in range(len(scurrent)):
			res.append(scurrent[element2])

	#TODO Handle empty elements ?
	
	return res


""" splitListKeep() -> List of String

Does the same thing as splitKeep() for a List of String.
"""
def splitListKeep(strlist, char):

	scopy = []
	if not(isinstance(strlist, list)):
		scopy.append(strlist)
	else: 
		scopy = strlist
	parts = ("","","")
	res = []
	for element in range(len(scopy)):
		while (scopy[element].find(char) != -1):
			parts = scopy[element].partition(char)
			if (parts[0] != ""):
				res.append(parts[0])
			res.append(parts[1])
			scopy[element] = parts[2]
		if (scopy[element] != ""):
			res.append(scopy[element])

	return res



""" stripList() -> List

Iterates strip() for each element of the parameter.
strip() removes all leading and trailing whitespace in a string.
"""
def stripList(strlist):
	for element in range(len(strlist)):
		strlist[element] = strlist[element].strip()
	return strlist


