def main(n: int = 100) -> int:
    sum_of_squares = sum(i**2 for i in range(n + 1))
    square_of_sum = (n * (n + 1) // 2) ** 2
    return square_of_sum - sum_of_squares


if __name__ == "__main__":
    print(main())
