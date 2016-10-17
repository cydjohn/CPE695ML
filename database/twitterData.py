# -*- coding: UTF-8 -*-  
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
		number = twitterData.find().count()
		print 'total twitts number: ' + str(number)
		return number

	def find_one(self,dataId):
		if twitterData.find_one({"id_str":dataId}) is None:
			return False
		return True

	def find(self,data):
		return twitterData.find({"user.id_str":data}) 

	def findUserById(self,userId):
		return  not twitterData.find_one({"user.id_str":userId}) is None

	def deleteOne(self,twittId):
		return twitterData.delete_one({"id_str": twittId}).deleted_count

	def deleteMany(self,data):
		twitterData.delete_many(data).deleted_count

	# def removeAllData(self):
	# 	twitterData.remove()