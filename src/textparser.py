#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function #UNIX systems : Disable default print function
import io



####################
# GLOBAL CONSTANTS #
####################
GLOBAL_SEP = "***" #Separates objects (used between each Unit or CO)
LINE_SEP = '\n'
ELEMENT_SEP = ';' #Separates elements
COMMAND_SEP = ':'


#######################
# CLASS : TEXT PARSER #
#######################
"""
Source content : File | List of List of String (2d String array)
int line_pointer
int word_pointer

The content is organized like this :
[ line_1,line_2,line_3, ...line_n ]
where lines are :
["CO_name"] <- 1st line of CO in CO_balance
["Effect_name ; COzone_size_and_type ; command_1 ; ... ; command_n"] <- 2nd line of CO in CO_balance
["COP_name ; command_1 ; ... ; command_n"] <- 3rd line of CO in CO_balance
["SCOP_name ; command_1 ; ... ; command_n"] <- 4th line of CO in CO_balance
["***"] <- Unit or CO separator
["Unit_name"] <- 1st line of Unit in Unit_balance
["cost movement movement_type fuel+x_per_turn vision weapon_code"] <- 2nd line of Unit in Unit_balance
["first_weapon_name : ammo attack_type range"] <- if weapon_code == 1 or 3 : 3rd line of Unit in Unit_balance
["second_weapon_name : attack_type range"] <- if weapon_code == 2 or 3 : 3rd or 4th line of Unit in Unit_balance
["command_1|property_1 ... command_n|property_n"] <- Last line of Unit in Unit_balance

"""

""" #OUTDATED
['***',
'Max\n',
'Attaque frontale',
'1+',
'bonus : +30/+0 direct_units',
'Max en force',
'increase_movement : 1 direct_units',
'Puissance max',
'increase_movement : 1 direct_units',
'bonus : +20/+0 direct_units',
'***', 'Misc\n', 'Effet', '0+', 'bonus : +0/+0 all', 'COP', 'bonus : +10/+10 all', 'SCOP', 'bonus : +20/+20 all', '***']			
"""

""" #THIS ONE
[['***'],
 ['Max'],
 ['Attaque frontale', '1+', 'bonus : +30/+0 direct_units'],
 ['Max en force', 'increase_movement : 1 direct_units'],
 ['Puissance max', 'increase_movement : 1 direct_units', 'bonus : +20/+0 direct_units'],
 ['***'],
 ['Misc'],
 ['Effet', '0+', 'bonus : +0/+0 all'],
 ['COP', 'bonus : +10/+10 all'],
 ['SCOP', 'bonus : +20/+20 all'],
 ['***']]


EX : ['Attaque frontale', '1+', 'bonus : +30/+0 direct_units'] is a line
'1+' is a word within this line
"""



class TextParser:

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

				#2) Split COs by GLOBAL_SEP, keeping GLOBAL_SEP as element
				content = splitListKeep(content, GLOBAL_SEP)
				content = stripList(content)

				#3) Split each line by ELEMENT_SEP
				#This returns a list of lists representing each "part" of a line
				for line in range(len(content)):
					content[line] = splitList(content[line], ELEMENT_SEP)
					content[line] = stripList(content[line])

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


	""" getNextWord() -> String

	A word is defined by a series of char until a separator. Default separators are defined at the beginning of this file. Or you can specify one by yourself. ?????

	Gets the word specified by the pointers. Checks once if indexes are wrong.
	If the word is GLOBAL_SEP -> returns the next word.
	If the end of file/line was atteined -> returns the empty String.

	"""
	def getNextWord(self):

		try:
			res = self.content[self.line_pointer][self.word_pointer]
			if (res == GLOBAL_SEP):
				self.line_pointer = self.line_pointer + 1
				self.word_pointer = 0
				res = self.content[self.line_pointer][self.word_pointer]
			else:
				self.word_pointer = self.word_pointer + 1
		except IndexError:
			res = ''
		return res



	""" getNextLine() -> List of String

	Get the line specified by the pointers. Does NOT advance.
	If the end of file was atteined -> returns an empty list.

	"""
	def getNextLine(self):

		try:
			res = self.content[self.line_pointer]
		except IndexError:
			res = ['']
		return res


	""" advNextLine()

	"""
	def advNextLine(self):

		self.line_pointer = self.line_pointer + 1
		self.word_pointer = 0



	""" isCommand() -> bool

	"""
	def isCommand(self, s):
		return (s.find(COMMAND_SEP) != -1)


	""" getCommand() -> (String, [List of String]) ***A DEPLACER***
		Ex. : -> ("bonus", ["+30/+0", "direct_units"])
	"""
	def getCommand(self):
		title = ''
		arg_list = []
		if not(endOfLine()):
			current_word = self.content[self.line_pointer][self.word_pointer].split(COMMAND_SEP)
			title = current_word[0]

			for i in range(1, len(current_word)):
				arg_list.append(current_word[i])
		return (title, [arg_list])


	# use getattr to call functions based on a string, ex. "my_func" -> call my_func()



	""" doCommand() ***A DEPLACER***

	Do a command as specified on AWBW_command_list. First argument must be the command name (else it returns CommandNameError), then a series of arguments which do not conflict with the command (else it returns CommandArgError).
	"""
	def doCommand(self):
		pass


	""" currentLineLength() -> int

	"""
	def currentLineLength(self):
		return len(self.content[self.line_pointer])


	""" endOfLine() -> bool

	"""
	def endOfLine(self):
		return (self.word_pointer >= len(self.content[self.line_pointer]))


	""" endOfFile() -> bool

	"""
	def endOfFile(self):
		return (self.line_pointer >= len(self.content))


	def display(self):
		print("Content = ", self.content, "\nLine = ", self.line_pointer, "\nWord = ", self.word_pointer)

	def displayAt(self, line, word):
		try:
			print("Content at line = ", line, " word = ", word, " is :\n", self.content[line][word])
		except IndexError:
			print("No word at this index")



###################
# OTHER FUNCTIONS #
###################

""" split() -> List of String

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
	element = 0
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
	#element = 0
	#while (element < len(res)) :
	#	if (res[element] == ""):
	#		del res[element]
	#	else:
	#		element = element+1

	
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
Then removes any empty element.
"""
def stripList(strlist):
	element = 0
	length = len(strlist)
	while (element < length):
	#for element in range(length):
		strlist[element] = strlist[element].strip()
		if strlist[element] == "":
			del strlist[element]
			length = length-1
		element = element+1
	return strlist




