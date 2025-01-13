
def fibonacci(n: int) -> list[int]:
    """
    Returnerar en lista med de första n Fibonacci-talen.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


print(fibonacci(10))  # Förväntat: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci(5))   # Förväntat: [0, 1, 1, 2, 3]
print(fibonacci(0))   # Förväntat: []
