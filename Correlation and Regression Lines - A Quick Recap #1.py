# Enter your code here. Read input from STDIN. Print output to STDOUT
# taken reference from https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html
# taken reference from https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/forum/comments/1441030

import math

# a = input()

x = "Physics Scores 15 12 8 8 7 7 7 6 5 3".split(" ")
y = "History Scores 10 25 17 11 13 17 20 13 9 15".split(" ")
# print(x, y)
new_x = [int(x[i]) for i in range(2, len(x))]
new_y = [int(y[i]) for i in range(2, len(y))]


n = len(new_x)
x_avg = sum(new_x)/n
y_avg = sum(new_y)/n
numerator = sum([(xi - x_avg)*(yi - y_avg) for xi, yi in zip(new_x, new_y)])
denominator = math.sqrt(sum((xi - x_avg)**2 for xi in new_x) * sum((yi - y_avg)**2 for yi in new_y))

corr_coef = numerator/denominator

print(round(corr_coef, 3))
