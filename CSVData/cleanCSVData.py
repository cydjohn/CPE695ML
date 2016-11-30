# coding: utf-8
import os
import pandas

class cleanCSVData(object):
	def cleanType(self,data):
		locationType = data["type"]
		locationAddress = set(data["address"])
		addressDic = {}
		count = 1
		for address in locationAddress:
			addressDic[address] = count 
			count += 1

		for num in range(0,len(data["type"])):
			if str(data["type"][num]).strip() == 'yes':
				data["type"][num] = addressDic[data["address"][num]]
			if str(data["placename"][num]).strip() == 'null':
				data["placename"][num] = addressDic[data["address"][num]]
		return data



	def cleanCSVData(self):
		path = "CSVData/" #文件夹目录  
		files= os.listdir(path) #得到文件夹下的所有文件名称  
		for file in files:
			if file[-3:]=='csv':
				data = pandas.read_csv(path+file)
				newData = self.cleanType(data)
				df = pandas.DataFrame(newData, columns = ['userid', 'time', 'longitude', 'latitude','osm_id','class','type','placename','address'])
				fileName = "cleanedCSVData/"+file
				self.writeDataToCSV(df,fileName)

	def writeDataToCSV(self,dataFlow,fleName):
		dataFlow.to_csv(fileName)

	def analysisData(self,data,userId):
		# time how many location data,  
		# how many types,  
		# 6-10 10-15 15-20 rest 
		# 每个时间段有多少记录 summary  
		# [清理数据? eg  building yes null ? 夜里出现频率 -> decide home or not] 
		# earth distance? maximum dis  how many days?
		numberOfLocationData = 0
		numberOfTypes = 0
		numberOfPeriod6_10 = 0
		numberOfPeriod10_15 = 0
		numberOfPeriod15_20 = 0
		numberOfPeriodRest = 0

#  from geopy.distance import vincenty
#  newport_ri = (41.49008, -71.312796)
#  cleveland_oh = (41.499498, -81.695391)
#  print(vincenty(newport_ri, cleveland_oh).miles)
		numberOfLocationData = data["address"].value_counts().count()
		numberOfTypes = len(set(data["type"]))
		for num in range(0,len(data["time"])):
			time = data["time"][num][11:-17]
			if (int(time)>=6 and int(time)<10):
				numberOfPeriod6_10 += 1
			elif (int(time)>=10 and int(time)<15):
				numberOfPeriod10_15 += 1
			elif (int(time)>=15 and int(time)<20):
				numberOfPeriod15_20 += 1
			else :
				numberOfPeriodRest += 1

		return {'numberOfLocationData':numberOfLocationData,'numberOfTypes':numberOfTypes,'numberOfPeriod6_10':numberOfPeriod6_10,'numberOfPeriod10_15':numberOfPeriod10_15,'numberOfPeriod15_20':numberOfPeriod15_20,'numberOfPeriodRest':numberOfPeriodRest,'userId':userId}
		print numberOfPeriodRest

		

if __name__ == '__main__':
	# cleanCSVData().cleanCSVData()

	path = "cleanedCSVData/" #文件夹目录  
	files= os.listdir(path) #得到文件夹下的所有文件名称  
	userData = []
	for file in files:
		if file[-3:]=='csv':
			data = pandas.read_csv(path+file)
			userData.append(cleanCSVData().analysisData(data,file[:-3]))
	df = pandas.DataFrame(userData, columns = ['numberOfLocationData', 'numberOfTypes', 'numberOfPeriod6_10', 'numberOfPeriod10_15','numberOfPeriod15_20','numberOfPeriodRest','userId'])
	fileName = "userData/"+"userData.csv"
	cleanCSVData().writeDataToCSV(df,fileName)
	print userData


	


