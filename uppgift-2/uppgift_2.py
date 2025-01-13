

from typing import List

def sum_list(numbers: List[int]) -> int:
    """
    Returnerar summan av alla siffror i listan.
    """
    return sum(numbers)


print(sum_list([1, 2, 3]))  # Förväntat resultat: 6
print(sum_list([]))         # Förväntat resultat: 0
print(sum_list([-1, -2, 3]))  # Förväntat resultat: 0

