
def filter_odd(numbers: list[int]) -> list[int]:
    """
    Returnerar en lista med alla jämna tal från den givna listan.
    """
    return [num for num in numbers if num % 2 == 0]


print(filter_odd([1, 2, 3, 4]))  # Förväntat resultat: [2, 4]
print(filter_odd([1, 3, 5]))     # Förväntat resultat: []
print(filter_odd([]))            # Förväntat resultat: []