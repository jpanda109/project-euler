from pemodule import *

x = str(factorial(100))
sum = 0
for i in range(len(x)):
    sum += int(x[i])

print sum
