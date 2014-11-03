i = 0
concact = 1
product = 1
while i <= 1000000:
    cstr = str(concact)
    for j in range(len(cstr)):
        i += 1
        if (i == 1 or i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000 or i == 1000000):
            product *= int(cstr[j])
    concact += 1

print(product)
