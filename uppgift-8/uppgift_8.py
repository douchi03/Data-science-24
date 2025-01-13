
def count_letters(string: str) -> dict:
    """
    Returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.
    """
    letter_count = {}
    for char in string:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


print(count_letters("hello"))  # Förväntat: {"h": 1, "e": 1, "l": 2, "o": 1}
print(count_letters(""))        # Förväntat: {}
print(count_letters("aaa"))     # Förväntat: {"a": 3}
