class ZeroDivisionEx(Exception):
    def __init__(self, dividend, divisor):
        self.__dividend = dividend
        self.__divisor = divisor

    def __str__(self):
        return f"Невозможно {self.__dividend} поделить на {self.__divisor}"


if __name__ == "__main__":
    while True:
        divident = int(input("Введите делимое: "))
        divisor = int(input("Введите делитель: "))
        if divisor == 0:
            print(ZeroDivisionEx(divident, divisor))
            continue
        if divident == "q" or divisor == "q":
            exit()
        print(f"Результат деления: {divident / divisor}")
