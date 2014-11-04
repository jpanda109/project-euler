def isPanProd(x, y, z):
    strx = str(x)
    stry = str(y)
    strz = str(z)
    strtotal = strx + stry + strz
    if len(strtotal) != 9 or strtotal.count('0') > 0:
        return False
    checkpan = []
    for i in range(9):
        if strtotal[i] in checkpan:
            return False
        checkpan.append(strtotal[i])
    return True

sum = 0
panProds = []
for i in range(823):
    for j in range(5000):
        h = i * j
        if h not in panProds and isPanProd(i, j, h):
            panProds.append(h)
            sum += h

print(sum)

