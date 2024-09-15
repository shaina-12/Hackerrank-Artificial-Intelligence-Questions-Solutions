# Enter your code here. Read input from STDIN. Print output to STDOUT
# taken reference from https://www.hackerrank.com/challenges/stat-warmup/forum/comments/1450643
# taken reference from https://stackoverflow.com/questions/27222079/converting-a-single-line-string-to-integer-array-in-python
import numpy as np

def mode(values):
    values.sort()
    dictValues = {}
    for i in range(len(values)):
        if values[i] not in dictValues:
            dictValues[values[i]] = 1
        else:
            dictValues[values[i]] += 1
    max_val = 1
    ind_max_val = -1;
    for x, y in dictValues.items():
        if y > max_val:
            max_val = y
            ind_max_val = x
    if ind_max_val == -1:
        print(values[0])
    else:
        print(ind_max_val)
    
    # if max_val > 1:
    #     for x, y in dictValues.items():
    #         if y == max_val:
    #             print(x, end=" ")
    #     print()
    # else:
    #     print(values[0])

def confidenceInterval(values, num):
    x_mean = np.mean(values)
    x_std = np.std(values)
    interval = 1.96 * (x_std / (num ** 0.5))
    lower, upper = x_mean - interval, x_mean + interval
    print(round(lower, 1), round(upper, 1))

num = int(input())
values = list(map(int, input().split(" ")))
#print(values)
print(round(np.mean(values),1))
print(round(np.median(values),1))
mode(values)
print(round(np.std(values), 1))
confidenceInterval(values, num)
