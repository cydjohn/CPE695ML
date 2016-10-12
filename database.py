from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter']
twitterData = db['twitterData']
class MLDatabase():	
	def addData(self,data):
		twitterData.insert_one(data)

	def getAllData(self):
		return twitterData.find()
		# return twitterData.find_one({"author" : "Mike" })

	def getAllDataNumber(self):
		return twitterData.find().count()

	def find_one(self,dataId):
		if twitterData.find_one({"id_str":dataId}) is None:
			return False
		return True

	def testdata(self):
		post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": "lalalal"}
		post_id = twitterData.insert_one(post).inserted_id
		print post_id

	def removeAllData(self):
		twitterData.remove()
