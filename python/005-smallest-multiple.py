def smallestMultiple(n: int, res=1):
    n += 1  # this range is inclusive
    sieve = [0, 0] + [1] * (n - 2)
    for i in range(n):
        if sieve[i]:
            sieve[i**2 :: i] = [0] * len(sieve[i**2 :: i])
            # sieve[i**2 :: i] = [0] * ((n - i**2 - 1) // i + 1)
            power = i
            while i * power < n:
                power *= i
            res *= power
    return [0, res][n > 1]


print(smallestMultiple(20))
