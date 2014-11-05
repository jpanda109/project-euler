import time

start = time.time()

def findNextNumber(x):
    num = 0;
    while x > 0:
        num += (x%10)**2
        x = int(x / 10)
    return num

class chain_dict(dict):
    def __missing__(self, key):
        return 2

chain = chain_dict()

chain[89] = 1
chain[1] = 0

count = 0
for i in range(1, 10000000):
    x = i
    while chain[x] == 2:
        y = findNextNumber(x)
        if chain[y]:
            chain[i] = 1
        elif not chain[y]:
            chain[i] = 0
        x = y
    if chain[i] == 1:
        count += 1

print(count)

print("Time elapsed", time.time() - start)
