from functools import cache


def main(n: int = 1000000) -> int:
    @cache
    def collatz(i: int) -> int:
        if i == 1:
            return 1
        elif i % 2 == 0:
            i //= 2
        else:
            i = i * 3 + 1
        return collatz(i) + 1

    return max(range(1, n), key=collatz)


if __name__ == "__main__":
    print(main())
