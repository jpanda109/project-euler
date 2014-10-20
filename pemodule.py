#takes a positive integer and returns whether it is prime or not
def isPrime(x):
    assert x > 0
    if x <= 1:
        return False
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            return False
    return True;

#returns the factorial of a number
def factorial(x):
    assert x >= 0
    if x <= 1:
        return 1
    return x * factorial(x - 1)

#returns the combination of two number e.g. 5C3
#the combination of two numbers is defined as n!/(k!(n-k)!)
#the combination applies to the amount of order unspecific arrangments
#   there are for a given option
#   for example, you have 3 apple and 5 baskets to put them in, how many
#   arrangements are there?
def combination(n, k):
    assert n >= 0 and n >= k
    return (factorial(n) / (factorial(k) * factorial(n-k)))

#returns the permuation of two numbers e.g. 5P3
#the permutation of two numbers is defines as n!/(n-k)!
#the permutation applies to the amount of order specific arrangements
#   there are for a given option
#   for example, you have 3 apples of different colors and 5 baskets to
#   put them in, how many arrangements are there?
def permutation(n, k):
    assert n >= 0 and n >= k
    return (factorial(n) / (factorial(n-k)))

#returns the nth number in the fibonacci sequence
def fibonacci(n):
    assert n > 0
    if n == 1 or n == 2:
        return 1
    return (fibonacci(n-1) + fibonacci(n-2))

#returns whether or not x is palindromes
def isPalindrome(x):
    return str(x) == str(x)[::-1]
