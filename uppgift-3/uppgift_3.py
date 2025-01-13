

def max_in_list(numbers: list[int]) -> int:
    """
    Returnerar det största talet i listan.
    """
    if not numbers:
        raise ValueError("Listan är tom")
    
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value


lista = [1, 3, 7, 2, 5]
print(f"Det största talet är: {max_in_list(lista)}")
