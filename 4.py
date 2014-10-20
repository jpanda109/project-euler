from pemodule import *
largest = 0;
for i in range(100, 1000):
    for j in range(100, 1000):
        k = i * j
        if isPalindrome(k):
            if k>largest:
                largest = k

print(largest)

