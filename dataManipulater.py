# -*- coding: UTF-8 -*- 
from netWork import MLTwitterAPI
from datamodel import *
from statisticalDiagram import *
from outPutData import *
import json

Twitter = MLTwitterAPI()
userDataModel = userDataModel()
twitterDataModel = twitterDataModel()
statisticalDg = MLStatisticalDiagram()
exportData = MLExportData()

def geatherUsers():
	Twitter.searchForUsers()

def geatherUserTimeline():
	for user in userDataModel.getAllUsers():
		Twitter.getUserTimelineByUserId(user["id_str"])

def deleteUselessUser():
	userDataModel.deleteUselessUserById()

def showNumberOfUsersAndTwitts():
	twitterDataModel.getAllTwittsNumber()
	userDataModel.getAllUsersNumber()

def countUserWteets():
	result = []
	for user in userDataModel.getAllUsers():
		result.append(twitterDataModel.countUserTweets(user["id_str"]))
	return result

def getDatas():
	geatherUsers()
	geatherUserTimeline()
	deleteUselessUser()
	showNumberOfUsersAndTwitts()

def getDaysAndTweetsOfUser():
	numberOfTweets = []
	days = []
	for user in userDataModel.getAllUsers():
		data = twitterDataModel.getDaysAndTweetsPerUser(user["id_str"])
		numberOfTweets.append(data[0])
		days.append(data[1])
	return [numberOfTweets,days]
  

def drawHistogram():
	statisticalDg.drawHistogramWithArray(countUserWteets())

def drawScatterPlots():
	deleteUselessUser()
	data = getDaysAndTweetsOfUser()
	statisticalDg.drawScatterPlotsWithXY(data[1],data[0])

def exportDataToCSV():
	
	for user in userDataModel.getAllUsers():
		userId = []
		time = []
		longitude = []
		latitude = []
		data = twitterDataModel.getTimeLongituteLatitutePerUser(user["id_str"])
		for d in data:
			userId.append(user["id_str"])
			time.append(d[1])
			longitude.append(d[2])
			latitude.append(d[3])
		rowData = {'userId':userId, 'time':time, 'longitude':longitude, 'latitude':latitude}
	# print rowData
		exportData.toCSV(rowData,user["id_str"])


if __name__ == "__main__":

	exportDataToCSV()

	
	    



	