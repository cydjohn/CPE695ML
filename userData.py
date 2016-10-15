from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter']
userData = db['userData']
class MLUserDatabase():	
	def addData(self,data):
		userData.insert_one(data)

	def getAllData(self):
		return userData.find()
		# return userData.find_one({"author" : "Mike" })

	def getAllDataNumber(self):
		number = userData.find().count()
		print 'total user number: ' + str(number)
		return number

	def find_one(self,dataId):
		if userData.find_one({"id_str":dataId}) is None:
			return False
		return True

	def removeAllData(self):
		userData.remove()

	def deleteUserById(self,uesrId):
		userData.delete_one({"id_str":uesrId})
