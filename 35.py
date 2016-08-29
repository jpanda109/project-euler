import math
import itertools

mem = {}

def is_prime(n):
    if n in mem:
        return mem[n]
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            mem[n] = False
            return mem[n]
    mem[n] = True
    return mem[n]

def permutations
