from pemodule import *

sum = 0
for i in range(3, 7 * factorial(9)):
    j = str(i)
    tempsum = 0
    for x in range(len(j)):
        h = factorial(int(j[x]))
        tempsum += h
    if tempsum == i:
        print(i)
        sum += i

print(sum)
