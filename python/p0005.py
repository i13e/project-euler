def main(n: int = 20, res: int = 1) -> int:
    gcd = lambda x, y: gcd(y, x % y) if y else x
    for i in range(1, n + 1):
        res *= i // gcd(i, res)
    return res


if __name__ == "__main__":
    print(main(20))
