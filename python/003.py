def main(target: int = 600851475143) -> int:
    """
    Calculate the largest prime factor of a given target.

    Args:
        target (int, optional): The number for which to find the 
            largest prime factor. Defaults to 600851475143.

    Returns:
        int: The largest prime factor of the target.
    """

    for num in range(2, int(target**0.5) + 1):
        while target % num == 0:
            # Print only the largest prime factor
            if target == num:
                return num
            target //= num

    # If the loop ends, the target is prime
    return target


if __name__ == "__main__":
    try:
        target = int(input("Enter the target number: "))
        result = main(target)
        print(f"Largest Prime Factor: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
