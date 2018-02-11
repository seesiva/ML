"""
Five number summary example
"""
import numpy as np
# Students who has scored in Tamil Language
tamilMarks = np.array([82,74,56,35,89,78,90,100,84,65,54,59,45])
tukey = [np.min(tamilMarks),
          np.percentile(tamilMarks, 25, interpolation='midpoint'),
          np.median(tamilMarks),
          np.percentile(tamilMarks, 75, interpolation='midpoint'),
          np.max(tamilMarks)]
for v in tukey:
     print(v)