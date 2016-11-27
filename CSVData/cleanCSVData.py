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



	def readCSVData(self):
		path = "CSVData/" #文件夹目录  
		files= os.listdir(path) #得到文件夹下的所有文件名称  
		for file in files:
			if file[-3:]=='csv':
				data = pandas.read_csv(path+file)
				newData = self.cleanType(data)
				df = pandas.DataFrame(newData, columns = ['userid', 'time', 'longitude', 'latitude','osm_id','class','type','placename','address'])
				fileName = "cleanedCSVData/"+file
				df.to_csv(fileName)

if __name__ == '__main__':
	cleanCSVData().readCSVData()

	


