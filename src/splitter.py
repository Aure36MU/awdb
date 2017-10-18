def splitListKeep(strlist, char): # return List of String

	scopy = []
	#DONE find a way to handle simple string
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


def splitKeep(s, char): # return List of String

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


def splitList(strlist, char): # return List of String
	scopy = []
	#DONE find a way to handle simple string
	if not(isinstance(strlist, list)):
		scopy.append(strlist)
	else: 
		scopy = strlist

	res = []
	for element in range(len(scopy)):
		scurrent = scopy[element].split(char)

		for element2 in range(len(scurrent)):
			res.append(scurrent[element2])

	#TODO Handle empty elements ?

	for element in range(len(res)):
		res[element] = res[element].strip()
	
	return res



def stripList(strlist): # return List
	for element in range(len(strlist)):
		strlist[element] = strlist[element].strip()
	return strlist


