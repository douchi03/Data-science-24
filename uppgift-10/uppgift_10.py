
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Konverterar en temperatur från Celsius till Fahrenheit.
    """
    return (celsius * 9/5) + 32


print(celsius_to_fahrenheit(0))     # Förväntat: 32
print(celsius_to_fahrenheit(100))   # Förväntat: 212
print(celsius_to_fahrenheit(-40))   # Förväntat: -40