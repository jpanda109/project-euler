f = open('p067_triangle.txt', 'r')

lines = []
for line in f:
    lines.append(line)

triangle = []
for i in range(len(lines)):
    triangle.append([int(x) for x in lines[i].split()])

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        if triangle[i+1][j] > triangle[i+1][j+1]:
            triangle[i][j] += triangle[i+1][j]
        else:
            triangle[i][j] += triangle[i+1][j+1]

print(triangle[0])
