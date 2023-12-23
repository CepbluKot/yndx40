import math


a = int(input())
b = int(input())
n = int(input())


if a > math.ceil(b / n):
    print('Yes')
else:
    print('No')
