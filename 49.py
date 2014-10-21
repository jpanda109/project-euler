from pemodule import *

def isPermutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def fn2p(x):
    dlimit = int((10000 - x)/2) + 1
    for i in range(x + 1, x + dlimit):
        if isPrime(x) and isPermutation(x, i) and isPrime(i) and isPermutation(x, 2*i-x) and isPrime(2*i-x):
            print x, i, 2*i-x

for i in range(1000, 10000):
    fn2p(i)
