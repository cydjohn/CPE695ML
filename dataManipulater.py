from database import MLDatabase
from twitterAPI import MLTwitterAPI
import json

db= MLDatabase()
Twitter = MLTwitterAPI()


if __name__ == "__main__":
	# Twitter.searchForUsers()
	# data = {'user_id': 211, 'name': 'Luke'}
	# print db.addData(data)
	# for d in db.getAllData():
	# 	# d.pop('_id', None)
	# 	print d["id"]
	# 	print json.dumps(d, indent=4, sort_keys=True)
	# print db.find_one("45716372")
	# print db.removeAllData()

	print db.getAllDataNumber()
