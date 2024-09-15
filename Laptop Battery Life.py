#!/bin/python3
# taken reference from https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
# taken reference from https://www.hackerrank.com/challenges/battery/editorial

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    timeCharged = float(input().strip())
    files = open('trainingdata.txt')
    text = files.readlines()
    x = []
    y = []
    for i in range(len(text)):
        xi, yi = map(float, text[i].split(','))
        if xi < 4:
            x.append(xi)
            y.append(yi)
    files.close()
    n = len(x)
    x_avg = sum(x)/n
    y_avg = sum(y)/n
    numerator = 0
    denominator = 0
    for i in range(n):
        x_diff = x[i] - x_avg
        numerator += (x_diff * (y[i] - y_avg))
        denominator += (x_diff ** 2)
    b = (1.0 * numerator) / denominator
    a = y_avg - (b * x_avg)
    if timeCharged < 4:
        val = a + (b * timeCharged)
        print(round(val, 2))
    else:
        print(8)
