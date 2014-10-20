def findNext(x):
    if x%2==0:
        return x/2
    return 3*x+1

def chainLength(x):
    if x == 1:
        return 1
    return chainLength(findNext(x)) + 1

start = 1
longest = 0
for i in range(1, 1000000):
    c = chainLength(i)
    if c > longest:
        start = i
        longest = c

print(start)
