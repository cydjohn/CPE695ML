# coding:utf-8
from sklearn import svm
import os
import pandas


class MLPredict(object):
	def readCSVData(self):
		path = "cleanedCSVData/" #文件夹目录  
		files= os.listdir(path) #得到文件夹下的所有文件名称  
		for file in files:
			if file[-3:]=='csv':
				data = pandas.read_csv(path+file)
				self.trainData(data)

	def trainData(self,data):
		X = []
		Y = data["placename"]
		# print data["time"]
		for num in range(0,len(data["time"])):
			day = self.setDay(data["time"][num][:3])
			time = data["time"][num][11:-17]
			print time
			X.append([day,time,data["class"][num],data["type"][num]])
		clf = svm.SVC()
		clf.fit(X, Y)
	def setDay(self,day):
		days = {
		'Mon':1,
		'Tue':2,
		'Wed':3,
		'Thu':4,
		'Fri':5,
		'Sat':6,
		'Sun':7
		}
		return days[day]



if __name__ == '__main__':
	MLPredict().readCSVData()