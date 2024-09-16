# Enter your code here. Read input from STDIN. Print output to STDOUT
# taken reference from https://github.com/shaina-12/Hackerrank-Artificial-Intelligence-Questions-Solutions/blob/main/Correlation%20and%20Regression%20Lines%20-%20A%20Quick%20Recap%201.py
# taken reference from https://github.com/shaina-12/Hackerrank-Artificial-Intelligence-Questions-Solutions/blob/main/Laptop%20Battery%20Life.py

import math

x = "Physics Scores 15 12 8 8 7 7 7 6 5 3".split(" ")
y = "History Scores 10 25 17 11 13 17 20 13 9 15".split(" ")
# print(x, y)
new_x = [int(x[i]) for i in range(2, len(x))]
new_y = [int(y[i]) for i in range(2, len(y))]


n = len(new_x)
x_avg = sum(new_x)/n
y_avg = sum(new_y)/n
numerator = 0
denominator = 0

for i in range(n):
    x_diff = new_x[i] - x_avg
    numerator += (x_diff * (new_y[i] - y_avg))
    denominator += (x_diff ** 2)
    
slope = (1.0 * numerator)/denominator

print(round(slope, 3))
