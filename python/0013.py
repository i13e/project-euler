def main():
    with open("resources/0013_numbers.txt") as f:
        numbers = [int(line) for line in f]
    return str(sum(numbers))[:10]


if __name__ == "__main__":
    print(main())
