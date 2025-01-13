
def word_count(text: str) -> int:
    """
    Returnerar antalet ord i en given text.
    """
    return len(text.split())


print(word_count("hello world"))              # Förväntat: 2
print(word_count(""))                        # Förväntat: 0
print(word_count("Python är fantastiskt!"))  # Förväntat: 3