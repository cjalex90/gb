my_list = []

while True:  # Actually while not EOF
    try:
        my_list.append(input("Введите значение для добавления в список: "))
    except EOFError:
        break

for number, value in enumerate(my_list):
    if number and (number % 2):
        tmp = None
        tmp = my_list[number - 1]
        my_list[number - 1] = value
        my_list[number] = tmp

print(my_list)
