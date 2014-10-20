x = 1
y = 2

sum = 2
while x <= 4000000 and y <= 4000000:
    z = x + y
    x = y
    y = z
    if z%2==0 and z <= 4000000:
        sum += z

print(sum)
