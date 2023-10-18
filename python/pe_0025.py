def main(n: int = 1000):
    a, b, i = 1, 0, 1
    while a < 10 ** (n - 1):
        a, b, i = a + b, a, i + 1
    return i


if __name__ == "__main__":
    print(main())
