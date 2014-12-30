def isIncreasing(x):
    first = x % 10
    while x >= 10:
        x /= 10
        if first < x % 10:
            return False
        first = x % 10
    return True

def isDecreasing(x):
    first = x % 10
    while x >= 10:
        x /= 10
        if first > x % 10:
            return False
        first = x % 10
    return True

def isBouncy(x):
    return not isIncreasing(x) and not isDecreasing(x)

bouncy = 0
notbouncy = 0
x = 0
while bouncy == 0 or bouncy != notbouncy * 99:
    x +=1 
    if (isBouncy(x)):
        bouncy += 1
    else:
        notbouncy += 1

print(x)
