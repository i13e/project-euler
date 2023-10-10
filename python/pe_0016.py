def main(n=2**1000) -> int:
    return sum(int(c) for c in str(n))


if __name__ == "__main__":
    print(main())
