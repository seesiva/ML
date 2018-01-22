"""
PCA - Principal Component Analysis
"""
import pandas as pd
from matplotlib import pyplot as plt


def main():
    data = pd.read_csv("sampledata.csv",skiprows=1, header=None)
    data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]  # rename column names to be similar to R naming convention
    data.V1 = data.V1.astype(str)
    pd.tools.plotting.scatter_matrix(data.loc, diagonal="kde")
    plt.tight_layout()
    plt.show()
    