def sameDigits(x, y):
    if len(str(x)) != len(str(y)):
        return False
    digitX = []
    dlen = len(str(x))
    for i in range(dlen):
        if x%10 in digitX:
            return False
        digitX.append(x%10)
        x /= 10
    for i in range(dlen):
        if y%10 not in digitX:
            return False
        y /= 10
    return True

x = 1
while True:
    if sameDigits(x, 2*x) and sameDigits(x, 3*x) and sameDigits(x, 4*x) and sameDigits(x, 5*x) and sameDigits(x, 6*x):
        break
    x += 1

print x
