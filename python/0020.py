from math import factorial

def main(n: int = 100) -> int:
    return sum(map(int, str(factorial(n))))


if __name__ == "__main__":
    print(main())
