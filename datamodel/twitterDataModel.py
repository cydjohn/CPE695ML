# -*- coding: UTF-8 -*-  
from database import MLTwitterDatabase

twitterdb = MLTwitterDatabase()

class twitterDataModel(object):
	"""docstring for MLTwitterDatabase"""
	def insertUserDataIntoDatabase(self,data):
		if twitterdb.find_one(data["id_str"]) is False:
			twitterdb.addData(data)
			print 'new twitts added!! id: ' + str(data["id"])
			print data["geo"]

	def deleteUselessTwitt(self):
		for d in twitterdb.getAllData():
			if d["geo"]["coordinates"] == [-0.0244, 37.9039]:
				print d["user"]["id"]
		# print twitterdb.deleteMany({"geo.coordinates":[-0.0244, 37.9039]})
		# print 

	def getAllTwittsNumber(self):
		twitterdb.getAllDataNumber()
		