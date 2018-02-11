"""
Five number summary example
"""
import numpy as np
# Students who has scored in Tamil Language
tamilMarks = np.array([82,74,56,35,89,78,90,100,84,65,54,59,45])
summaryTitles = ["Min","Lower Quartile", "Median", "Upper Quartile", "Maximum"]
tukey = [np.min(tamilMarks),
          np.percentile(tamilMarks, 25, interpolation='midpoint'),
          np.median(tamilMarks),
          np.percentile(tamilMarks, 75, interpolation='midpoint'),
          np.max(tamilMarks)]
for index, v in enumerate(tukey):
    print(summaryTitles[index], ':',v)
