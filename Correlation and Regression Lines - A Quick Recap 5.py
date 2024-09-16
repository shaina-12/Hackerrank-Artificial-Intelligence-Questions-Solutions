# Enter your code here. Read input from STDIN. Print output to STDOUT
# taken reference from https://www.hackerrank.com/challenges/correlation-and-regression-lines-4/forum
# taken reference from https://www.hackerrank.com/challenges/correlation-and-regression-lines-5/forum
# taken reference from https://www.hackerrank.com/challenges/correlation-and-regression-lines-5/forum/comments/937953

sigma_x = 3

slope2 = 20/9

slope1 = 5/4

sigma_y = ((3**2) * (slope2/slope1))

print(round(sigma_y, 1))
