from twitterData import MLTwitterDatabase

twitterdb = MLTwitterDatabase()

class twitterDataModel(object):
	"""docstring for MLTwitterDatabase"""
	def insertUserDataIntoDatabase(self,data):
		if twitterdb.find_one(data["id_str"]) is False:
			twitterdb.addData(data)
			print data["geo"]
		