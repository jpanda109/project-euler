from math import *

sum = 0
for i in range(1, 1001):
    sum += i**i
    sum %= 10000000000

sumstr = str(sum)
while len(sumstr) < 10:
    sumstr = '0' + sumstr
print(sumstr)
