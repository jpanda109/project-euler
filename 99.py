import math

f = open('p099_base_exp.txt', 'r')

pairs = f.read().split('\n')
pairs = [pairs[i].split(',') for i in range(len(pairs))]

high = 0
lineNumber = 0
logbase = float(pairs[0][1])
for i in range(len(pairs)):
    cur = math.log(float(pairs[i][0]), logbase) * float(pairs[i][1])
    if cur > high:
        high = cur
        lineNumber = i

# increment by 1 to account for 0-based indexing
print(lineNumber + 1)
f.close()
