class Instance:
		values = {} #dictionary entries
		@property  #the actual classification of the Instance
		def Classification(self):
			return self.values['class']
		def __init__(self):
			self.values = {}



def parseLine(line): #parses variables on an @ line

	line = line.replace ('@', '')
	wordList = line.split("\t") #put each word into list 
	return wordList


def parseDataFile(dataFile):
	listofVariables = []
	listOfInstances = []
	file = open (dataFile, 'rU')
	fileLines = file.readlines()

	#remove whitespace from files
	for line in fileLines:
		line= line.rstrip()
		if line:
			if line[0] == '#':   #check for comment
				x =2
			elif line[0] == '@':	 #check for attribute
				listofVariables = parseLine(line)
			else:				# handle data
				tempInstance = Instance()
				valueList = parseLine(line)
				if len(listofVariables) < 1:
					print "Bad Data File"
					break

				for attr, value in zip(listofVariables, valueList):
					tempInstance.values[attr] = value
				listOfInstances.append(tempInstance)


				# listOfInstances.append(Instance())

				# valueList = parseLine(line)
				# for attr,value in zip(listofVariables, valueList):
				# 	print attr + ":" + value
				# 	listOfInstances[-1].values[attr] = value
	print listOfInstances			
	return listOfInstances

filePath = "/home/hack/Programming/Rbes/data.txt"

listOfInstances = parseDataFile(filePath)

print listOfInstances[0].values