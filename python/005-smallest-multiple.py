def smallestMultiple(target):
    res = 1
    for num in range(2, target + 1):
        # Remove composite numbers
        if res % num == 0:
            continue
        # Reduce perfect powers into primes
        for prime in range(2, int(num**0.5) + 1):
            if num % prime == 0:
                num = prime
                break
        # Multiply result by the remaining prime
        res *= num
    return res


print(smallestMultiple(20))
