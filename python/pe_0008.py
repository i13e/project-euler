def main():
    with open("resources/0008_series.txt") as f:
        digits = f.read().replace("\n", "")

    res = 0
    for i in range(len(digits) - 13):
        product = 1
        for j in range(13):
            product *= int(digits[i + j])
        res = max(res, product)
    return res


if __name__ == "__main__":
    print(main())
