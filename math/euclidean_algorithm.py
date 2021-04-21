def euclidean_algorithm(a: int, b: int) -> int:
    """Implementation of Euclidean Algorithm.
    Returns the greatest common divisor of two numbers.
    """
    while b > 0:
        reminder = a % b
        a = b
        b = reminder
    return a
