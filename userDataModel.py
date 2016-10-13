from userData import MLUserDatabase

userdb= MLUserDatabase()

class userDataModel(object):
	"""docstring for userDataModel"""
	def insertUserDataIntoDatabase(self,data):
		if userdb.find_one(data["id_str"]) is False:
			userdb.addData(data)
			print data

		

