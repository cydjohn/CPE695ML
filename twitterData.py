from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter']
twitterData = db['twitterData']
class MLTwitterDatabase():	
	def addData(self,data):
		twitterData.insert_one(data)

	def getAllData(self):
		return twitterData.find()

	def getAllDataNumber(self):
		return twitterData.find().count()

	def find_one(self,dataId):
		if twitterData.find_one({"id_str":dataId}) is None:
			return False
		return True

	def removeAllData(self):
		twitterData.remove()