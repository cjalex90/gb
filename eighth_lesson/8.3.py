class NotIntEx(Exception):
    def __init__(self, num: str):
        self.num = num

    def __str__(self):
        return f"{self.num} не является числом"


if __name__ == "__main__":
    numbers_list = []
    while (number := input("Введите число: ")) != "stop":
        if not number.isdigit():
            print(NotIntEx(number))
        else:
            numbers_list.append(number)
    print(f"Введены числа: {', '.join(numbers_list)}")
