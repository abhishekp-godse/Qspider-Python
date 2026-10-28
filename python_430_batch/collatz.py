def collatz(n: int) -> list[int]:
    """Generate the Collatz sequence starting from a positive integer n."""
    if n < 1:
        raise ValueError("Starting number must be a positive integer.")
    
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        
    return sequence