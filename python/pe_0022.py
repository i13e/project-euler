def main():
    with open("resources/0022_names.txt", "r") as file:
        names = file.read().replace("\"", '').split(",")

    res = 0
    for i, name in enumerate(sorted(names), start=1):
        res += sum(ord(c) - ord("A") + 1 for c in name) * i

    return res


if __name__ == "__main__":
    print(main())
