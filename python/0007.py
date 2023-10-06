def main(n: int = 10_001) -> int:
    primes = [2]
    i = 3
    while len(primes) < n:
        if all(i % p for p in primes if p**2 <= i):
            primes.append(i)
        i += 2

    return primes[-1]


if __name__ == "__main__":
    print(main())
