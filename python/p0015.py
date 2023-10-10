from functools import cache


@cache
def main(r: int = 20, c: int = 20) -> int:
    if not (r and c):
        return 1
    return main(r - 1, c) + main(r, c - 1)


if __name__ == "__main__":
    print(main())
