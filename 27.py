from pemodule import *

maxPrimeAmount = 0
realA = 0
realB = 0
for a in range(-1000, 999):
    for b in range(-1000, 999):
        unfinished = True
        n = 0
        primeAmount = 0
        while unfinished:
            qformula = n**2 + a * n + b
            if (qformula > 0 and isPrime(qformula)):
                primeAmount += 1
                n += 1
                continue
            unfinished = False
        if (primeAmount > maxPrimeAmount):
            maxPrimeAmount = primeAmount
            realA = a
            realB = b

print realA * realB
