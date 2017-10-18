def splitKeep(strlist, char):
	scopy = strlist
	"""#TODO find a way to handle simple string
	scopy = []
	if not(isinstance(strarray, list)):
		scopy.append(strarray)
	else: 
		for i in range(len(strarray)):
			scopy.append(strarray[i])"""
	parts = ("","","")
	res = []
	for element in range(len(scopy)):
		while (scopy[element].find(char) != -1):
			parts = strarray[element].partition(char)
			if (parts[0] != ""):
				res.append(parts[0])
			res.append(parts[1])
			scopy[element] = parts[2]
		if (scopy[element] != ""):
			res.append(scopy[element])
		
	return res
