
def multiplication_table(n: int, limit: int) -> list[int]:
    """
    Returnerar multiplikationstabellen för n upp till limit i en lista.
    """
    return [n * i for i in range(1, limit + 1)]


print(multiplication_table(2, 3))  # Förväntat resultat: [2, 4, 6]
print(multiplication_table(3, 5))  # Förväntat resultat: [3, 6, 9, 12, 15]
print(multiplication_table(5, 0))  # Förväntat resultat: []
