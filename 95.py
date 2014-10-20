def findDivisorSum(x):
    sum = 0
    for i in range(1, x/2+1):
        if x%i == 0:
            sum += i
    return sum

def findChainLength(x):
    original = x
    length = 1
    x = findDivisorSum(x)
    if (x > 999999):
        return 0
    while (original != x):
        x = findDivisorSum(x)
        if (x > 999999):
            return 0
        length+=1
    return length


