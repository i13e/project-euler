def main(lo: int = 1, hi: int = 1001) -> int:
    assert lo < hi < 1_000_000
    def f(n: int) -> str:
        if n < 20:
            return ONES[n]
        elif n < 100:
            tens, rest = divmod(n, 10)
            return f"{TENS[tens]}{ONES[rest]}"
        elif n < 1000:
            hundreds, rest = divmod(n, 100)
            return f"{ONES[hundreds]}hundred{f'and{f(rest)}' * bool(rest)}"
        else:
            thousands, rest = divmod(n, 1000)
            return f"{f(thousands)}thousand{f(rest)}"

    return sum(len(f(n)) for n in range(lo, hi))
ONES = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
# ONES = [len(i) for i in ONES]
# TENS = [len(i) for i in TENS]


if __name__ == "__main__":
    print(main())

# print(numWords(342961758))
