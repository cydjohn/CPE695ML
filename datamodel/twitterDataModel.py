# -*- coding: UTF-8 -*-  
from database import MLTwitterDatabase
import json

twitterdb = MLTwitterDatabase()

class twitterDataModel(object):
	"""docstring for MLTwitterDatabase"""
	def insertUserDataIntoDatabase(self,data):
		if twitterdb.find_one(data["id_str"]) is False:
			twitterdb.addData(data)
			print 'new tweet added!! id: ' + str(data["id"])
			print data["geo"]

	def deleteUselessTwitt(self):
		for d in twitterdb.getAllData():
			if d["geo"]["coordinates"] == [-0.0244, 37.9039]:
				print d["user"]["id"]
		# print twitterdb.deleteMany({"geo.coordinates":[-0.0244, 37.9039]})
		# print 
	def countUserTweets(self,userId):
		return twitterdb.getTweetsListByUserId(userId).count()

	def getAllTwittsNumber(self):
		twitterdb.getAllDataNumber()

	def getTweetsListByUserId(self,userId):
		return twitterdb.getTweetsListByUserId(userId)

	def getDaysAndTweetsPerUser(self,userId):
		time = []
		for a in twitterdb.getTweetsListByUserId(userId):
			a["_id"] = 'asdf'
			if(a["created_at"].split(' ')[1] == 'Oct'):
				time.append(a["created_at"].split(' ')[2])
			print json.dumps(a, indent=4, sort_keys=True)

		time.sort()
		if(len(time)>0):
			return [len(time),int(time[-1]) - int(time[0])]
		else:
			return [0,0]


		