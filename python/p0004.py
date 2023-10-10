from itertools import combinations

def main(lo: int = 100, hi: int = 1_000) -> int:
    return max(x * y for x, y in combinations(range(lo, hi), 2) if str(x * y) == str(x * y)[::-1])


if __name__ == "__main__":
    print(main())
