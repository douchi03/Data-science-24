
def validate_password(password: str) -> bool:
    """
    Kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
    """
    return len(password) >= 8 and any(char.isdigit() for char in password)


print(validate_password("abc12345"))  # Förväntat resultat: True
print(validate_password("short"))      # Förväntat resultat: False
print(validate_password("password1"))  # Förväntat resultat: True
print(validate_password("password"))   # Förväntat resultat: False