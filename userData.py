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
		return userData.find().count()

	def find_one(self,dataId):
		if userData.find_one({"id_str":dataId}) is None:
			return False
		return True

	def testdata(self):
		post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": "lalalal"}
		post_id = userData.insert_one(post).inserted_id
		print post_id

	def removeAllData(self):
		userData.remove()
