def main(limit=4e6, a=0, b=1):
    """
    Calculate the sum of even Fibonacci numbers below a given limit.

    Args:
        limit (float, optional): Upper limit for Fibonacci numbers.
        a (int, optional): First term in the Fibonacci sequence.
        b (int, optional): Second term in the Fibonacci sequence.

    Returns:
        int: Sum of even Fibonacci numbers below the target.
    """
    res = 0
    while a <= limit:
        a, b = b, a + b
        if a % 2 == 0:
            res += a
    return res


if __name__ == "__main__":
    try:
        target = float(input("Enter the target value: "))
        result = main(target)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
