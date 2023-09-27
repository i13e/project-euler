def main(limit: int = 1000) -> int:
    """
    Calculate the sum of all natural numbers below a given limit that are
    divisible by 3 or 5.

    Args:
        limit (int): The upper limit (exclusive) for natural numbers to
            consider.

    Returns:
        int: The sum of all natural numbers below the limit that are
            divisible by 3 or 5.
    """
    return sum(i for i in range(limit) if not (i % 3 and i % 5))


if __name__ == "__main__":
    try:
        limit = int(input("Enter the limit: "))
        result = main(limit)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
