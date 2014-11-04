from pemodule import *

def d2b(x):
    return int(bin(x)[2:])

def isDoublebasePal(x):
    return isPalindrome(x) and isPalindrome(d2b(x))

sum = 0
for i in range(1, 1000000):
    if isDoublebasePal(i):
        sum += i

print(sum)
