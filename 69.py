from pemodule import *

n = 1
i = 2
while n <= 1000000:
    if isPrime(i):
        n *= i
    i += 1

print(n/(i-1))
