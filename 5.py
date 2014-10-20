def isDivisible1to20(x):
    for i in range(11, 21):
        if x%i != 0:
            return False
    return True

n = 1
while isDivisible1to20(n) == False:
    n += 1

print(n)

#Alternatively
print(2*3*4*5*6*7*11*13*17*19)
