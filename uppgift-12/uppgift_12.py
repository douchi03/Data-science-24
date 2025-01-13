def create_student_register(students: list[tuple[str, int]]) -> dict:
    """
    Tar emot en lista med namn och ålder och returnerar en dictionary
    där namnet är nyckeln och åldern är värdet.
    """
    return {name: age for name, age in students}


students = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
print(create_student_register(students))  # Förväntat: {"Anna": 20, "Bertil": 25, "Cecilia": 22}
