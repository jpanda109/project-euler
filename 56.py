def digitSum(x):
    s = 0
    while x > 0:
        s += x % 10
        x /= 10
    return s

maxx = 0
x = 0
for i in range(1, 100):
    for j in range(1, 100):
        x = i ** j
        d = digitSum(x)
        if d > maxx:
            maxx = d

print maxx
