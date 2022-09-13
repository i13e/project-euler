def smallestMultiple(target):
    res = 1
    for num in range(2, target + 1):
        # Remove composite numbers
        if res % num == 0:
            continue

        # Simplify prime squares
        for prime in range(2, int(num ** (0.5)) + 1):
            while num % prime == 0:
                if num == prime:
                    break
                num //= prime
        # Multiply result by the remaining prime
        res *= num
    return res


print(smallestMultiple(20))
