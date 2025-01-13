
def is_palindrome(string: str) -> bool:
    """
    Kontrollerar om en given sträng är ett palindrom (samma framifrån och bakifrån).
    """
    return string == string[::-1]


print(is_palindrome("radar"))    # Förväntat: True
print(is_palindrome("python"))   # Förväntat: False
print(is_palindrome(""))          # Förväntat: True
print(is_palindrome("level"))    # Förväntat: True
