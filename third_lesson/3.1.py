def division(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return e


a = int(input("Введите число - делимое : "))
b = int(input("Введите число - делитель: "))

print(division(a, b))
