f = open('p022_names.txt')

namestring = f.read()[1:-1]

names = namestring.split("\",\"")

names.sort()

total = 0
for i in range(len(names)):
    sum = 0
    for j in range(len(names[i])):
        sum += ord(names[i][j]) - 64

    total += sum * (i + 1)

print total

f.close()

