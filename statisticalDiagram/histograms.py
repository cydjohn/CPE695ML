import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py

class MLHistogram(object):
	"""docstring for MLHistogram"""
	def drawHistogramWithArray(self,data):
		plt.figure()
		plt.hist(data)
		# plt.hist(data,bins=[0,300,600,900])
		plt.title("Tweets Histogram")
		plt.xlabel("tweets")
		plt.ylabel("User number")
		plt.show()
		plt.savefig("histogram")