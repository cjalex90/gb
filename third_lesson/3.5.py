escape_char = "q"


def get_sum(list_of_nums):
    return sum(map(int, list_of_nums))


result = 0

while True:
    mylist = input("Введите числа через пробел для подсчета суммы: ").split()
    try:
        if escape_char in mylist:
            mylist.remove(escape_char)
            result += get_sum(mylist)
            break
        else:
            result += get_sum(mylist)
    except ValueError:
        print("Нужно вводить только числа!")

print(f"Сумма всех введенных чисел: {result}")

