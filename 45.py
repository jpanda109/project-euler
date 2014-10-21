triangleList = [1]
pentagonalList = [1]
hexagonalList = [1]

unfinished = True
i = 2
while unfinished:
    triangleList.append(i*(i+1)/2)
    pentagonalList.append(i*(3*i-1)/2)
    hexagonalList.append(i*(2*i-1))
    if triangleList[i-1] in pentagonalList and triangleList[i-1] in hexagonalList and triangleList[i-1] != 40755:
        unfinished = False
    i+=1

print triangleList[i-2]
