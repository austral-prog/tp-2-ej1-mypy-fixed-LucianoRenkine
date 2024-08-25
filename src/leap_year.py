def is_leap_year():
    year: int = int(input("> Ingrese un año: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"El año {year} es bisiesto")
        return True
    else:
        print(f"El año {year} no es bisiesto")
        return False
