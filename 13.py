f = open('p013_numbers.txt', 'r')

numbers = []
for line in f:
    numbers.append(int(line))

sum = 0
for i in range(100):
    sum += numbers[i]

print(str(sum)[:10])
