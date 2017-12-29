"""
Python based KNN approach
"""
import csv
import os
import random
import math
import operator

ROOTDIR = "D:\\MV\\Projects\\ml\\mlprogs\\data"
TRAINING_SET = []
TEST_SET = []
EU_TEST_DATA1=[2,2,2,'a']
EU_TEST_DATA2=[4,4,4,'b']
TRAIN_SET=[[2,2,2,'a'],[6,7,5,'b'],[14,14,14,'c']]
TEST_INSTANCE = [5, 5, 5]
K = 1

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
def euclidean_distance(inst_one, inst_two, length):
    """
    Calculate euclidean distance
    """
    distance = 0
    for x in range(length):
        distance += pow((inst_two[x]-inst_one[x]), 2)
    return math.sqrt(distance)

def get_neighbors(training_set, test_instance, k):
    """
    Get Neighbours
    """
    distances = []
    length = len(test_instance)-1
    for x in range(len(training_set)):
        dist = euclidean_distance(test_instance, training_set[x], length)
        distances.append((training_set[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distances[x][0])
    return neighbours

def get_response(neighbors):
    """
    Get response based on the votes through the classification votes
    """
    classvotes = {}
    print range(len(neighbors))
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classvotes:
            classvotes[response] += 1
        else:
            classvotes[response] = 1
    sortedvotes = sorted(classvotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedvotes[0][0]

load_dataset('iris.data', 0.65, TRAINING_SET, TEST_SET)
distance=euclidean_distance(EU_TEST_DATA1,EU_TEST_DATA2,3)
print 'Train: ' + repr(len(TRAINING_SET))
print 'Test: ' + repr(len(TEST_SET))
print 'Distance:'+repr(distance)

#neighbors = get_neighbors(TRAIN_SET, TEST_INSTANCE, K)
#print(neighbors)

neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = get_response(neighbors)
print(response)
