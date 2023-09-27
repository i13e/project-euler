def main(min: int = 100, max: int = 1000, res: int = 0) -> int:
    """
    Find the largest palindrome that is a product of two numbers within a given
    range.

    Args:
        min (int, optional): The minimum value for the range. Defaults to 100.
        max (int, optional): The maximum value for the range. Defaults to 1000.
        res (int, optional): The initial result value. Defaults to 0.

    Returns:
        int: The largest palindrome that is a product of two numbers within the
        specified range.
    """
    for x in reversed(range(min, max)):
        for y in reversed(range(min, max)):
            if x * y <= res:
                break
            num, rev = x * y, 0
            while num:
                rev = rev * 10 + num % 10
                num //= 10
            if x * y == rev:
                res = x * y
                break
    return res


if __name__ == "__main__":
    try:
        min_val = int(input("Enter the minimum value: "))
        max_val = int(input("Enter the maximum value: "))
        result = main(min_val, max_val)
        print(f"Largest Palindrome Product: {result}")
    except ValueError:
        print("Invalid input. Please enter integers for the range.")
