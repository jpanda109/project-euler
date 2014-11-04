triangle = []
def populateTriangleList(x):
    for i in range(1, x + 1):
        triangle.append(i * (i + 1) / 2)

def getWordValue(x):
    value = 0
    for i in range(len(x)):
        value += ord(x[i]) - 64
    return value


populateTriangleList(40)

f = open('p042_words.txt', 'r')

string = f.read()
words = string.split("\",\"")
words[0] = (words[0])[1:]
words[len(words) - 1] = (words[len(words) - 1])[:-1]

count = 0
for i in range(len(words)):
    if getWordValue(words[i]) in triangle:
        count += 1

print count
