def multiply(a, b) -> int:
    if type(a) != int: raise ValueError("Аргументы должны быть int")
    if type(b) != int: raise ValueError("Аргументы должны быть int")
    return a * b
