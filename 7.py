from pemodule import *

count = 0
n = 1

while count != 10001:
    n += 1
    if isPrime(n) == True:
        count += 1

print(count)
print(n)
