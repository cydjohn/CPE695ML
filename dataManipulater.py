# -*- coding: UTF-8 -*-  
from userData import MLUserDatabase
from twitterData import MLTwitterDatabase
from twitterAPI import MLTwitterAPI
from userDataModel import userDataModel
import json

userdb= MLUserDatabase()
twitterdb = MLTwitterDatabase()
Twitter = MLTwitterAPI()
userDataModel = userDataModel()

def geatherUsers():
	Twitter.searchForUsers()

def geatherUserTimeline():
	for d in userdb.getAllData():
		Twitter.getUserTimelineByUserId(d["id_str"])

def deleteUselessUser():
	userDataModel.deleteUselessUserById()

def showNumberOfUsersAndTwitts():
	twitterdb.getAllDataNumber()
	userdb.getAllDataNumber()

if __name__ == "__main__":

	geatherUsers()
	geatherUserTimeline()
	showNumberOfUsersAndTwitts()
	# deleteUselessUser()



	