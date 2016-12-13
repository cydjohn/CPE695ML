# coding:utf-8
from sklearn import svm
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

import os
import pandas

dataClassDic = {}
dataTypeDic = {}
dataPlaceDic = {}

total = []

class MLPredict(object):

	def setClassAndTypeAndPalceSet(self,data):
		
		dataClassSet = set(data["class"])
		dataTypeSet = set(data["type"])
		dataPlaceSet = set(data["placename"])
		i = 0
		for a in dataClassSet:
			dataClassDic[a] = i
			i+=1
		i = 0
		for a in dataTypeSet:
			dataTypeDic[a] = i
			i+=1
		i = 0
		for a in dataPlaceSet:
			dataPlaceDic[a] = i
			i+=1

	def replaceClass(self,dataClass):
		return dataClassDic[dataClass]

	def replaceType(self,dataType):
		return dataTypeDic[dataType]

	def replacePlace(self,dataPlace):
		return dataPlaceDic[dataPlace]

	def readCSVData(self):
		path = "cleanedCSVData/" #文件夹目录  
		files= os.listdir(path) #得到文件夹下的所有文件名称  
		for file in files:
			if file[-3:]=='csv':
				data = pandas.read_csv(path+file)
				self.trainData(data)

	def trainData(self,data):
		train = int(len(data)*0.75)
		predict = len(data) - train
		X = []
		Y = []
		self.setClassAndTypeAndPalceSet(data)
		# print data["time"]
		for num in range(0,len(data["time"])):
			day = self.setDay(data["time"][num][:3])
			time = data["time"][num][11:-17]

			X.append([day,int(time),self.replaceClass(data["class"][num]),self.replaceType(data["type"][num])])
			Y.append(self.replacePlace(data["placename"][num]))


		# clf = svm.SVC()
		# clf = GaussianNB()
		# clf = KNeighborsClassifier()
		# clf = DecisionTreeClassifier()
		clf = LogisticRegression()


		clf.fit(X[:train], Y[:train])
		r = Y[:predict]
		p = clf.predict(X[:predict])
		count = 0.0
		for a in range(0,predict):
			if(r[a]==p[a]):
				count+=1
				
		total.append(count/predict)
		# print count/predict * 100

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

	print sum(total)/float(len(total)) * 100
