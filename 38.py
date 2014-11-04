def conProd(x, n):
    concact = ""
    for i in range(1, n+1):
        concact += str(x * i)
    return concact

def isPandigital(x):
    if len(x) != 9:
        return False
    pan = []
    for i in range(len(x)):
        if x[i] in pan or x[i] == '0':
            return False
        pan.append(x[i])
    return True

high = 0
for i in range(2, 10000):
    for j in range(2, 10):
        con = conProd(i, j)
        if len(con) > 9:
            continue
        if isPandigital(con) and int(con) > high:
            high = int(con)

print(high)

