def primeFactor(target):
    # Divide target by 2 until it is odd
    while target % 2 == 0:
        target /= 2

    # target is now odd, so we can skip even numbers
    for num in range(3, int(target ** (0.5)) + 1, 2):
        while target % num == 0:
            target /= num
        # Print only the largest prime factor
        if target == 1:
            return num
    # If loop ends, target is prime
    if target > 2:
        return target


print(primeFactor(600851475143))
