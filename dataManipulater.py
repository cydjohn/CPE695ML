# -*- coding: UTF-8 -*- 
from netWork import MLTwitterAPI
from datamodel import *
import json

Twitter = MLTwitterAPI()
userDataModel = userDataModel()
twitterDataModel = twitterDataModel()

def geatherUsers():
	Twitter.searchForUsers()

def geatherUserTimeline():
	for user in userDataModel.getAllUsers():
		Twitter.getUserTimelineByUserId(user["id_str"])

def deleteUselessUser():
	userDataModel.deleteUselessUserById()

def showNumberOfUsersAndTwitts():
	twitterDataModel.getAllTwittsNumber()
	userDataModel.getAllUsersNumber()

def countUserWteets():
	for user in userDataModel.getAllUsers():
		twitterDataModel.countUserTweets(user["id_str"])

if __name__ == "__main__":
	# twitterDataModel.deleteUselessTwitt()
	# geatherUsers()
	# geatherUserTimeline()
	# deleteUselessUser()
	# showNumberOfUsersAndTwitts()
	result = {}
	for d in countUserWteets():
		# if d not in result:
		# 	result[d] = 0 
		# result[d] += 1


	for key,value in result():  
		print key + ":%d" % value     



	