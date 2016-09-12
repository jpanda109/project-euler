primes = [2, 3, 4, 7]
squares = [(1, 1)]

def is_prime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True

def written_as_sum(n):
    for prime in primes:
        (last_square, last_squared) = squares[-1]
        while prime + 2 * last_square < n:
            new_square = last_square+1
            squares.append(((new_square, new_square ** 2)))
            (last_square, last_squared) = squares[-1]
        for (square, squared) in squares:
            total = prime + 2 * squared
            if n == total:
                return True
            elif total > n:
                break
    return False

if __name__ == '__main__':
    n = 3
    while True:
        if is_prime(n):
            primes.append(n)
        else:
            if not written_as_sum(n):
                break
        n += 2
    print(n)
