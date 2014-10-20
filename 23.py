a = 1
b = 1
c = 0
i = 2
while len(str(c)) < 1000:
    i+=1
    c = a + b
    a = b
    b = c

print i
