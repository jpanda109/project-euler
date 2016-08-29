def simplify(num, dem):
    i = 2
    while i <= num:
        if num % i == 0 and dem % i == 0:
            num //= i
            dem //= i
        else:
            i += 1
    return num, dem

def is_digit_cancelling(num, dem):
    num_digits = (num//10, num%10)
    dem_digits = (dem//10, dem%10)
    new_num, new_dem = simplify(num, dem)
    if num_digits[0] == dem_digits[1]:
        return (
            num_digits[1] % new_num == 0 and \
            dem_digits[0] % new_dem == 0 and \
            new_dem // new_num == dem_digits[0] // num_digits[1]
            )
    elif num_digits[1] == dem_digits[0]:
        return (
            num_digits[0] % new_num == 0 and \
            dem_digits[1] % new_dem == 0 and \
            new_dem // new_num == dem_digits[1] // num_digits[0]
            )
    else:
        return False
if __name__ == '__main__':
    num_prod = 1
    dem_prod = 1
    for dem in range(10, 100):
        for num in range(10, dem):
            if is_digit_cancelling(num, dem):
                print(num, dem)
                num_prod *= num
                dem_prod *= dem
    print(simplify(num_prod, dem_prod)[1])
