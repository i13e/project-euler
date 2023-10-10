def main(perimeter: int = 1_000) -> int:
    for a in range(1, perimeter):
        for b in range(a + 1, perimeter):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return -1


if __name__ == "__main__":
    print(main())
