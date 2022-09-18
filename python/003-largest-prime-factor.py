def primeFactor(target):
    for num in range(2, int(target**0.5) + 1):
        while target % num == 0:
            # Print only the largest prime factor
            if target == num:
                return num
            target //= num

    # If loop ends, target is prime
    return target


print(primeFactor(600851475143))
