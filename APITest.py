# -*- coding: UTF-8 -*-  
from TwitterAPI import TwitterAPI
import json
api = TwitterAPI("sRVZEM6K02ovYJ0At147BpGbu", "w85lyM2ZAZrBzuxlgtVG2H4BUJJbeLQ7fnLxA1hCCLeXRl2hhj", "772828862942175232-EohaQboJpvZkor7bt0argGggkAwh2mo", "pD1auN2XIVWFtQl84mbQW8FU2rugGTuZEoVDVVFlNVkZW")


r = api.request('search/tweets', {'q':'place NY'})
for item in r:
    print item


# API to get location  user_id
# r = api.request('users/lookup',{'user_id':319950150})
# res = json.loads(r.text)
# print res[0]["location"]

# r = api.request('statuses/user_timeline',{'user_id':319950150})
# res = json.loads(r.text)
# print res[0]