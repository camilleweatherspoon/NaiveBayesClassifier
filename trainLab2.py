#Camille Weatherspoon and Kaleb Glass
#CIS 474: Lab 2 - Naïve Bayes Classifier
#Created: 26/9/2013
#Last Modified: 26/9/2013

def train(filePath)
	#parse Instances into list
	totalNumInstances = 0
	print grade(instances, totalNumInstances)


def sort(instance)
	probSum = 0
	classesProb = totalCounts
	
	for c in classesProb.keys
		for i in instance
			for a in i.values.keys
				probSum = probSum + log(getValueCount(a, i.values[a], c))
		classesProb[c] = probSum
		probSum = 0
	
	
	#Whichever probability in classes is higher is the key that is returned
	
def grade(instanceList, totalNumInstances)
	gradeSum = 0
	for i in instanceList
		if(i.values['class'] == sort(i))
			gradeSum = gradeSum + 1
	return (gradeSum / totalNumInstances)
	
if __name__ == '__main__':
	train(filePath)
