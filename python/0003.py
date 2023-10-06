def main(n: int = 600_851_475_143) -> int:
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            if n == i:
                return i
            n //= i
    return n


if __name__ == "__main__":
    print(main())
