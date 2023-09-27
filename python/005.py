def main(n: int = 20, res: int = 1):
    """
    Find the smallest positive number that is evenly divisible by all integers
    from 1 to a given number n.

    Args:
        n (int, optional): The upper limit (inclusive) for the range of integers
            to consider. Defaults to 20.
        res (int, optional): The initial result value. Defaults to 1.

    Returns:
        int: The smallest number divisible by all integers from 1 to n.
    """
    n += 1  # This range is inclusive
    sieve = [0, 0] + [1] * (n - 2)
    for i in range(n):
        if sieve[i]:
            sieve[i**2 :: i] = [0] * len(sieve[i**2 :: i])
            power = i
            while i * power < n:
                power *= i
            res *= power
    return res * n > 1


if __name__ == "__main__":
    try:
        n_value = int(input("Enter the value of n: "))
        result = main(n_value)
        print(f"Smallest Number: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
