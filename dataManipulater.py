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
	print userdb.getAllDataNumber()

def geatherUserTimeline():
	for d in userdb.getAllData():
		# d.pop('_id', None)
		# print json.dumps(d, indent=4, sort_keys=True)
		Twitter.getUserTimelineByUserId(d["id_str"])

def deleteUselessUser():
	userDataModel.deleteUselessUserById()

if __name__ == "__main__":

	geatherUsers()
	geatherUserTimeline()
	twitterdb.getAllDataNumber()
	userdb.getAllDataNumber()
	# deleteUselessUser()

	# for d in twitterdb.getAllData():
	# 	userDataModel.insertUserDataIntoDatabase(d["user"])


	