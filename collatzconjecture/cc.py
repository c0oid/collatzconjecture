def collatz_conjecture(n: int) -> list:
    """
    Generates a Collatz sequence starting from a positive integer 'n'.
    The sequence is formed by applying the following rules:
    - If the number is even, the next number is half of that number.
    - If the number is odd, the next number is 3 times the number plus 1.
    The sequence ends when it reaches 1.
    """
    if n <= 0:
        raise ValueError("Invalid input: provide a positive integer")

    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq