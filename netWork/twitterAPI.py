# -*- coding: UTF-8 -*-  
from TwitterAPI import TwitterAPI
import json
from datamodel import *


userModel = userDataModel()
twitterModel = twitterDataModel()

# fanxiao
api = TwitterAPI("YgsQDGjL81nHTHu2hmXTfpvlx", "rn6tGwEsLRHiD4qUF3AvLVIaA3z3xolUZmWXtO6rKDDNbvCdWa", "1621725078-TaZJpo2o9vRLljpQKLojR1OJEOmhVFNSJjx4Uc2", "JmYWcmwBNSaixb0wC80nCzxDUh794odqzfiuR6gt4JBBF")

# houxiao
# api = TwitterAPI("W8NTyH7gPrpHqarHAN7wgLmfS", "RcRb3pfmroL4HM2vdkOVbQ1pKU2UGvFcZEaB1X1LTljxDsB9KE", "787382500775567360-ejMvvlX2eMuqKpsfPJTfeYm5XVFNNVn", "oxkblc1iVzbKUwlUoZNlMLsg6Q4Z39GckmnpdhOJbZxxT")

# aojia
# api = TwitterAPI("TtbTJVlxNchNPpBNhNVpqmxp1", "ard2JXdId7JkRM057JHe9RQkfmFWfMFSvscYyzTV6T10OYxhi4", "2686608859-Xl3s3B0fjk6Te7D2lC8l7eChKwKFaTgTyFZqzaU", "pcJYLNB3lNbsd2PuZJUc2L18Xd1GraomxD81FKpgPs4Zp")

# ziheng
# api = TwitterAPI("s45hPkpXAlWSMnwu7pqftpVRa", "nNBUIbXr8428DzQatmFIobJ3Bd67JUTSqzkYES1RlJXHuTPpUd", "787306318826799104-Q81JDS0Vz70W7hSBTqZkUeywx9r7FX2", "s3DLsZRVMolwQOhbqeOG7lt2DJP7RMfJPTduNZcp3xUFK")

# yudong
# api = TwitterAPI("sRVZEM6K02ovYJ0At147BpGbu", "w85lyM2ZAZrBzuxlgtVG2H4BUJJbeLQ7fnLxA1hCCLeXRl2hhj", "772828862942175232-EohaQboJpvZkor7bt0argGggkAwh2mo", "pD1auN2XIVWFtQl84mbQW8FU2rugGTuZEoVDVVFlNVkZW")

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
			print res
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
			except Exception as e:
				print data
				print 'user id:' + userId
				raise e