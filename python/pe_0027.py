from functools import cache


def main() -> int:
    @cache
    def is_prime(n: int) -> bool:
        return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

    def count_primes(a: int, b: int) -> int:
        return next(n for n in range(1000) if not is_prime(n**2 + a * n + b))

    nums = ((a, b, a * b) for a in range(-999, 1000, 2) for b in range(2, 1001))
    return max(nums, key=lambda x: count_primes(x[0], x[1]))[-1]


if __name__ == "__main__":
    print(main())
