from collections import Counter


def main(n: int = 500) -> int:
    def get_divisors(num: int) -> int:
        divisors = Counter()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors[i] += 1
                divisors[num // i] += 1
        return sum(divisors.values())

    i = 1
    triangle = count = 0
    while count < n:
        triangle += i
        count = get_divisors(triangle)
        i += 1
    return triangle


if __name__ == "__main__":
    print(main())
