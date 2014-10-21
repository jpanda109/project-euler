from pemodule import *

def itp(x):
    length = len(str(x))
    l = x
    for i in range(1, length):
        if not isPrime(l%(10**i)):
            return False
    r = x
    for i in range(length):
        if not isPrime(r):
            return False
        r /= 10
    return True

tp = []
count = 0
x = 10
while count != 11:
    if itp(x):
        count += 1
        tp.append(x)
    x += 1

total = 0
for i in range(len(tp)):
    total += tp[i]

print total
