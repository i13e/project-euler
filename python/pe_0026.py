def main(n: int = 1000):
    def cycle_length(d: int) -> int:
        seen = {}
        x = 1
        for i in range(d):
            if x in seen:
                return i - seen[x]
            seen[x] = i
            x = x * 10 % d
        return 0

    return max(range(1, n), key=cycle_length)


if __name__ == "__main__":
    print(main())
