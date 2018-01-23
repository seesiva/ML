"""
PCA - Principal Component Analysis
"""
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


def main():
	print "Principal Component Analysis"
	df = pd.read_csv("sampledata.csv",skiprows=1, header=None)
    	print "Completed reading data.."
	df.columns = ["V"+str(i) for i in range(1, len(df.columns)+1)] 
	print df.tail()
	pca = PCA(n_components=10)
    	pca.fit(df)
    	print(pca.explained_variance_ratio_)

if __name__ == '__main__':
	main()
