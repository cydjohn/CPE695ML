from database import MLDatabase

db= MLDatabase()

class userDataModel(object):
	"""docstring for userDataModel"""
	def insertUserDataIntoDatabase(self,data):
		if db.find_one(data["id_str"]) is False:
			db.addData(data)
			print data

		

