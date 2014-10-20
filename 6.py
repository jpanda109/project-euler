sumofsquares = 0
squareofsums = 0;

for i in range (1, 101):
    sumofsquares += i**2
    squareofsums += i

squareofsums*=squareofsums

print(squareofsums - sumofsquares)
