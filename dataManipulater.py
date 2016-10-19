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

if __name__ == "__main__":
	# twitterDataModel.deleteUselessTwitt()
	geatherUsers()
	geatherUserTimeline()
	deleteUselessUser()
	showNumberOfUsersAndTwitts()



	