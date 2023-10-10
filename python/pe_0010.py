def main(n: int = 2_000_000) -> int:
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i**2 :: 2 * i] = [False] * len(sieve[i**2 :: 2 * i])
    return sum([2] + [i for i in range(3, n, 2) if sieve[i]])


if __name__ == "__main__":
    print(main())
