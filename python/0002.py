def main(n: int = 4_000_000) -> int:
    def fibonacci():
        a, b = 0, 1
        while a <= n:
            yield a
            a, b = b, a + b
    return sum(filter(lambda x: x % 2 == 0, fibonacci()))


if __name__ == "__main__":
    print(main())
