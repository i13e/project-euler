from math import factorial


def main(n: int = 999_999) -> int:
    digits = list(range(10))
    res = 0

    for i in reversed(range(10)):
        index = n // factorial(i)
        n %= factorial(i)
        res = res * 10 + digits.pop(index)

    return res


if __name__ == "__main__":
    print(main())
