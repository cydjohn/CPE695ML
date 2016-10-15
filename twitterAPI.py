# -*- coding: UTF-8 -*-  
from TwitterAPI import TwitterAPI
import json
from userDataModel import userDataModel
from twitterDataModel import twitterDataModel


userModel = userDataModel()
twitterModel = twitterDataModel()

api = TwitterAPI("sRVZEM6K02ovYJ0At147BpGbu", "w85lyM2ZAZrBzuxlgtVG2H4BUJJbeLQ7fnLxA1hCCLeXRl2hhj", "772828862942175232-EohaQboJpvZkor7bt0argGggkAwh2mo", "pD1auN2XIVWFtQl84mbQW8FU2rugGTuZEoVDVVFlNVkZW")

class MLTwitterAPI(object):	
	def searchForUsers(self):
		queryKeyWords = ['New York','NY','NewYork']
		for q in queryKeyWords:
			r = api.request('search/tweets', {'q':q})
			for item in r:
				if self.getLocationBasedOnUserId(item["user"]["id"]):
					userModel.insertUserDataIntoDatabase(item["user"])
				# print json.dumps(item, indent=4, sort_keys=True)


	# API to get location  user_id
	def getLocationBasedOnUserId(self,userId):
		r = api.request('users/lookup',{'user_id':userId})
		res = json.loads(r.text)
		try:
			if res[0] is not None:
				res = res[0]["location"].lower()
		except Exception as e:
			raise
		return (('ny' in res) or ('new york' in res) or ('newyork' in res))

	def getUserTimelineByUserId(self,userId):
		r = api.request('statuses/user_timeline',{'user_id':userId})
		res = json.loads(r.text)
		# print json.dumps(res[0], indent=4, sort_keys=True)
		for data in res:
			try:
				if data["geo"] is not None:
					twitterModel.insertUserDataIntoDatabase(data)
					print 'new twitts added!! id: ' + str(data["id"])
			except Exception as e:
				print data
				print 'user id:' + userId
				raise e

				






