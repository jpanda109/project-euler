from pemodule import *

def shiftListElements(list, x, movement):
    a = list[x+movement]
    while movement > 0:
        list[x+movement] = list[x+movement-1]
        movement -= 1
    list[x] = a

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permutationNo = 1000000
factorialCounter = 9
listIndex = 9 - factorialCounter
while permutationNo != 1:
    for i in range(9):
        j = 9 - i
        movement = permutationNo / factorial(factorialCounter)
        if permutationNo - movement*factorial(factorialCounter) == 0:
            movement -= 1
        if movement > 0:
            permutationNo -= movement * factorial(factorialCounter)
            shiftListElements(numbers, listIndex, movement)
            break
    factorialCounter -= 1
    listIndex += 1

print numbers
