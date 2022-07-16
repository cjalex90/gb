number = int(input("Введите число: "))


max_digit = 0

while number:
    current_digit = number % 10
    if current_digit > max_digit:
        max_digit = current_digit
    number = number // 10

print(f"Максимальная цифра в числе: {max_digit}")