def divisorSum(x):
    sum = 0
    for i in range(2, int(x**.5) + 1):
        if x%i == 0:
            sum += i
            sum += x/i
    sum += 1
    return sum

sum = 0
x = []
for i in range(2, 10000):
    if i not in x:
        j = divisorSum(i)
        k = divisorSum(j)
        if i != j and i == k:
            x.append(i)
            x.append(j)
            sum += i + j

print(sum)
