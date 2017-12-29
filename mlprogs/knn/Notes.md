# KNN
k-Nearest Neighbors

# Notes
It is a competitive learning algorithm
It internally uses competition between model elements (data instances) in order to make a predictive decision

## References
1. https://www.quora.com/Classification-machine-learning-When-should-I-use-a-K-NN-classifier-over-a-Naive-Bayes-classifier
2. https://medium.com/@adi.bronshtein/a-quick-introduction-to-k-nearest-neighbors-algorithm-62214cea29c7

## List of reasons
1. When the dimensions are limited with more number of instances
2. When there is need for finding similarity
3. Recommendation systems
4. Typically for classification problems


## Approach:
k-NN solves the problem of prediction using data instances
Training observations will be part of the model.

## Dataset
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class: 
    -- Iris Setosa
    -- Iris Versicolour
    -- Iris Virginica

## Steps
1. Handle Data: Open the dataset from CSV and split into test/train datasets. - Completed
2. Similarity: Calculate the distance between two data instances. - Completed
3. Neighbors: Locate k most similar data instances. - Completed 
4. Response: Generate a response from a set of data instances. - Completed
5. Accuracy: Summarize the accuracy of predictions. - Completed
6. Main: Tie it all together. - Completed