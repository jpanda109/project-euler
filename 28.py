sum = 1
curAdd = 24
for i in range(int(1001/2)):
    sum += curAdd
    curAdd += 20 + (i+1) * 32

print(sum)
