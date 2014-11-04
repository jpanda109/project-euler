from pemodule import *

###populated text file with primes up to a million for easier debugging
#f = open('populateprimes.txt', 'w')
#for i in range(2, 500000):
#    if isPrime(i):
#        f.write(str(i))
#        f.write(" ")
#f.close()

f = open('populateprimes.txt', 'r')
primes = f.read().split()

length = 0
answer = 0
for i in range(len(primes)):
    debug = []
    curlength = 0
    sum = 0
    j = i
    while sum + int(primes[j]) < 1000000:
        debug.append(primes[j])
        sum += int(primes[j])
        j += 1
        curlength += 1
        if isPrime(sum) and curlength > length:
            length = curlength
            answer = sum

print(answer)
