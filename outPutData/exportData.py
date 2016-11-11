import pandas as pd

class MLExportData(object):
	"""docstring for MLExportData"""


	def toCSV(self,rowData,userId):
		df = pd.DataFrame(rowData, columns = ['userId', 'time', 'longitude', 'latitude'])
		fileName = "./CSVFile/"+userId +".csv"
		df.to_csv(fileName)