# Enter your code here. Read input from STDIN. Print output to STDOUT
# taken reference from https://www.geeksforgeeks.org/python-implementation-of-polynomial-regression/
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
n, train_size = tuple(map(int, input().split(" ")))
train_data = []
for i in range(train_size):
    train_data.append(list(map(float, input().split(" "))))
test_size = int(input())
test_data = []
for i in range(test_size):
    test_data.append(list(map(float, input().split(" "))))
train_data = np.array(train_data)
test_data = np.array(test_data)
train_features = train_data[:,:-1]
train_labels = train_data[:,-1]
poly = PolynomialFeatures(degree=3)
poly_train_features = poly.fit_transform(train_features)
poly_test_features = poly.fit_transform(test_data)
lr = LinearRegression()
lr.fit(poly_train_features, train_labels)
#print(poly_train_features.shape, poly_test_features.shape, train_labels.shape, train_features.shape, test_data.shape)
test_predict = lr.predict(poly_test_features)
for i in range(test_size):
    print(round(test_predict[i], 2))
