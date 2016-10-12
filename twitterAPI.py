# -*- coding: UTF-8 -*-  
from TwitterAPI import TwitterAPI
import json
from userDataModel import userDataModel

userModel = userDataModel()

api = TwitterAPI("sRVZEM6K02ovYJ0At147BpGbu", "w85lyM2ZAZrBzuxlgtVG2H4BUJJbeLQ7fnLxA1hCCLeXRl2hhj", "772828862942175232-EohaQboJpvZkor7bt0argGggkAwh2mo", "pD1auN2XIVWFtQl84mbQW8FU2rugGTuZEoVDVVFlNVkZW")

class MLTwitterAPI(object):	
	def searchForUsers(self):
		queryKeyWords = ['New York','NY']
		for q in queryKeyWords:
			r = api.request('search/tweets', {'q':q})
			for item in r:
				if self.getLocationBasedOnUserId(item["user"]["id"]):
					userModel.insertUserDataIntoDatabase(item["user"])
					# print item["user"]
				# print json.dumps(item, indent=4, sort_keys=True)


	# API to get location  user_id
	def getLocationBasedOnUserId(self,userId):
		r = api.request('users/lookup',{'user_id':userId})
		res = json.loads(r.text)
		if res[0] is not None:
			res = res[0]["location"].lower()
			pass

		return (('ny' in res) or ('new york' in res))


# r = api.request('statuses/user_timeline',{'user_id':319950150})
# res = json.loads(r.text)
# print res[0]

