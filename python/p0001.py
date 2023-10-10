def main(n: int = 1_000) -> int:
    return sum(i for i in range(n) if not (i % 3 and i % 5))


if __name__ == "__main__":
    print(main())
