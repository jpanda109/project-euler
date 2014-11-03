sum = 0
for i in range(2, 5 * (9**5)):
    j = str(i)
    tmpsum = 0
    for x in range(len(j)):
        h = int(j[x])
        tmpsum += h**5
    if tmpsum == i:
        sum += i

print(sum)
