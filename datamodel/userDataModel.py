# -*- coding: UTF-8 -*-  
from database import *

userdb= MLUserDatabase()
twitterdb = MLTwitterDatabase()

class userDataModel(object):
	"""docstring for userDataModel"""
	def insertUserDataIntoDatabase(self,data):
		if userdb.find_one(data["id_str"]) is False:
			userdb.addData(data)
			print 'new user added id:' + data["id_str"]

	def deleteUselessUserById(self):
		for d in userdb.getAllData():
			# print d["user"]["id_str"]
			if not twitterdb.findUserById(d["id_str"]):
				userdb.deleteUserById(d["id_str"])
				print 'delete user :' + d["id_str"]
			
		# 		userdb.deleteUserById(d["id_str"])
		# print 'lal'
	def getAllUsers(self):
		return userdb.getAllData()


	def getAllUsersNumber(self):
		userdb.getAllDataNumber()

