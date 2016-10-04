# -*- coding: UTF-8 -*-  
from twitter import *



t = Twitter(
    auth=OAuth('772828862942175232-EohaQboJpvZkor7bt0argGggkAwh2mo', 'pD1auN2XIVWFtQl84mbQW8FU2rugGTuZEoVDVVFlNVkZW', 'sRVZEM6K02ovYJ0At147BpGbu', 'w85lyM2ZAZrBzuxlgtVG2H4BUJJbeLQ7fnLxA1hCCLeXRl2hhj'))
# Get your "home" timeline
# print t.statuses.home_timeline()


# result = t.search.tweets(q="#NY")

# print result

# # Get a particular friend's timeline
# t.statuses.user_timeline(screen_name="billybob")

# # to pass in GET/POST parameters, such as `count`
# t.statuses.home_timeline(count=5)

# # to pass in the GET/POST parameter `id` you need to use `_id`
# t.statuses.oembed(_id=1234567890)

# # Update your status
# t.statuses.update(
#     status="Using @sixohsix's sweet Python Twitter Tools.")

# # Send a direct message
# t.direct_messages.new(
#     user="billybob",
#     text="I think yer swell!")

# # Get the members of tamtar's list "Things That Are Rad"
# t.lists.members(owner_screen_name="tamtar", slug="things-that-are-rad")

# # An *optional* `_timeout` parameter can also be used for API
# # calls which take much more time than normal or twitter stops
# # responding for some reason:
# t.users.lookup(
#     screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)

# # Overriding Method: GET/POST
# # you should not need to use this method as this library properly
# # detects whether GET or POST should be used, Nevertheless
# # to force a particular method, use `_method`
# t.statuses.oembed(_id=1234567890, _method='GET')

# # Send images along with your tweets:
# # - first just read images from the web or from files the regular way:
# with open("example.png", "rb") as imagefile:
#     imagedata = imagefile.read()
# # - then upload medias one by one on Twitter's dedicated server
# #   and collect each one's id:
# t_upload = Twitter(domain='upload.twitter.com',
#     auth=OAuth(token, token_secret, consumer_key, consumer_secret))
# id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
# id_img2 = t_upload.media.upload(media=imagedata)["media_id_string"]
# # - finally send your tweet with the list of media ids:
# t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))

# # Or send a tweet with an image (or set a logo/banner similarily)
# # using the old deprecated method that will probably disappear some day
# params = {"media[]": imagedata, "status": "PTT ★"}
# # Or for an image encoded as base64:
# params = {"media[]": base64_image, "status": "PTT ★", "_base64": True}
# t.statuses.update_with_media(**params)

# # Attach text metadata to medias sent, using the upload.twitter.com route
# # using the _json workaround to send json arguments as POST body
# # (warning: to be done before attaching the media to a tweet)
# t_upload.media.metadata.create(_json={
#   "media_id": id_img1,
#   "alt_text": { "text": "metadata generated via PTT!" }
# })