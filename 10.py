from pemodule import *

sum = 0

for i in range(2, 2000000):
    if isPrime(i):
        sum += i

print(sum)
