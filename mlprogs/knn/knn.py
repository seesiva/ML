"""
Python based KNN approach
"""
import csv
import os
import random

ROOTDIR = "D:\\MV\\Projects\\ml\\mlprogs\\data"
TRAINING_SET = []
TEST_SET = []


def load_dataset(file_name, split, training_set, test_set):
    """
    Load daset
    """
    with open(os.path.join(ROOTDIR, 'iris.data'), 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for row in range(len(dataset)-1):
            for col in range(4):
                dataset[row][col] = float(dataset[row][col])
            if random.random() < split:
                training_set.append(dataset[row])
            else:
                test_set.append(dataset[row])

load_dataset('iris.data', 0.66, TRAINING_SET, TEST_SET)
print 'Train: ' + repr(len(TRAINING_SET))
print 'Test: ' + repr(len(TEST_SET))
