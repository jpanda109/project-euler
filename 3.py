from pemodule import *

n = 600851475143
div = 2
while isPrime(n) == False:
    if n%div==0:
        n /= div
    else:
        div += 1

print(n)
