count = 0
for i in range(1, 10):
    power = 1
    result = i ** power
    while len(str(result)) >= power:
        if len(str(result)) == power:
            print(result, power)
            count += 1
            print (i, power)
        power += 1
        result = i ** power

print(count)
