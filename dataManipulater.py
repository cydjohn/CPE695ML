from userData import MLUserDatabase
from twitterData import MLTwitterDatabase
from twitterAPI import MLTwitterAPI
import json

userdb= MLUserDatabase()
twitterdb = MLTwitterDatabase()
Twitter = MLTwitterAPI()

def geatherUsers():
	Twitter.searchForUsers()
	print userdb.getAllDataNumber()



def geatherUserTimeline():
	# Twitter.getUserTimelineByUserId("82943769")
	for d in userdb.getAllData():
		# d.pop('_id', None)
		# print json.dumps(d, indent=4, sort_keys=True)
		Twitter.getUserTimelineByUserId(d["id_str"])


if __name__ == "__main__":
	geatherUsers()
	geatherUserTimeline()


	