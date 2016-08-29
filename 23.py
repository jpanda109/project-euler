import math

def is_abundant(n):
    res = 1
    for i in range(2, math.ceil(n**.5)):
        if n % i == 0:
            res += i + (n//i)
            if res > n:
                return True
    return False

def can_be_sum_of_2(n, lst1):
    for a in lst1:
        if a > n:
            break
        for b in lst1:
            t = a + b
            if t == n:
                return True
            elif t > n:
                break
    return False

if __name__ == '__main__':
    abundant_nums = []
    for i in range(1, 28123):
        if is_abundant(i):
            abundant_nums.append(i)
    res = 0
    for i in range(24, 28123):
        if can_be_sum_of_2(i, abundant_nums):
            res += i
    print(res)
