# -*- coding: UTF-8 -*- 
from netWork import MLTwitterAPI
from datamodel import *
from statisticalDiagram import *
import json

Twitter = MLTwitterAPI()
userDataModel = userDataModel()
twitterDataModel = twitterDataModel()
statisticalDg = MLHistogram()

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
	result = []
	for user in userDataModel.getAllUsers():
		result.append(twitterDataModel.countUserTweets(user["id_str"]))
	return result

if __name__ == "__main__":
	# twitterDataModel.deleteUselessTwitt()
	# geatherUsers()
	# geatherUserTimeline()
	# deleteUselessUser()
	# showNumberOfUsersAndTwitts()

	statisticalDg.drawHistogramWithArray(countUserWteets())
	    



	