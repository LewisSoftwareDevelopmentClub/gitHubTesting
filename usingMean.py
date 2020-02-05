import csv

# NEAREST NEIGHBOR ALGORITHM   KNN ALGORITHM
# IF N = 1 THEN FIND THE CLOSEST TRAINING DATA OBJECT FOR EACH TEST DATA OBJECT
# IF N > 1 THEN PICK THE LABEL BASED ON THE CONSENSUS OF THE N NEAREST TRAINING DATA OBJECTS,
# WHERE THE NEAREST DATA OBJECT WILL OVERULE IF THERE IS NO CONSENSUS


# Read in the
greScores = []

class DataObject :


	def __init__(self) :
		self.index = -1
		predictedResearch = False
		currentIndex = 0
		return

	def setGRE(self,dataItem) :
		# We assuming the data object is a string , and converting it into an integer
		self.greItem = int(dataItem)

	def setTOEFL(self,dataItem) :
		# We assuming the data object is a string , and converting it into an integer
		self.TOEFL = int(dataItem)

	def setChanceOfAdmit(self,dataItem) :
		self.coa = dataItem

	def setPrediction(self,dataItem) :
		if(dataItem is not None):
			self.prediction = int(dataItem)
		else:
			self.prediction = -1

	def setUnivRating(self,dataItem) :
		self.rating = int(dataItem)

	def setResearch(self,dataItem) :
		# This attribute is what we are prediciting from the test data instances.
		self.research = int(dataItem)



	# Add another member function in order to retrieve the TOEFL score.

myList = []

with open('Admission_Predict.csv') as csv_file :
	csv_reader = csv.reader(csv_file,delimiter=',')
	for index,row in enumerate(csv_reader) :
			if index == 0 :
				continue
			myDataObject = DataObject()
			myDataObject.setGRE(row[1])
			myDataObject.setTOEFL(row[2])
			# We assuming that we do not know the university rating
			# But we need read this in order to evaluate the predication
			myDataObject.setUnivRating(row[3])
			myDataObject.setResearch(row[7])
			myDataObject.setChanceOfAdmit(row[8])
			myDataObject.setPrediction(None)
			myList.append(myDataObject)



def findMean(column) :
	aggregateValue = 0
	for index,dataObject in enumerate(myList) :
		if column == 1 :
			aggregateValue += dataObject.greItem
		elif column == 2 :
			aggregateValue += dataObject.TOEFL

	return aggregateValue / len(myList)


result = findMean(2)
print(result)

	
