def smallestMultiple(target: int, res=1):
    if not target:
        return 0
    primes = [1] * (target + 1)
    primes[0] = primes[1] = 0
    for n in range(2, target + 1):
        if primes[n]:
            primes[n**2 : target + 1 : n] = [0] * (1 + (target - n**2) // n)
            power = 2
            while n ** power in range(target + 1):
                power += 1
            res *= n ** (power - 1)
    return res


print(smallestMultiple(20))
