def findNumDivisors(x):
    num = 0
    for i in range(1, int(x**.5) + 1):
        if x%i == 0:
            num += 2
    return num

solved = False
i = 2
x = 1
while not solved:
    x += i
    i += 1
    if findNumDivisors(x) > 500:
        print(x)
        solved = True
