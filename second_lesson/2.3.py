month = int(input("Введите номер месяца: "))

if month not in range(1, 13):
    print("Неверно введен номер месяца")

seasons = {
    "Зима": [12, 1, 2],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11]
}

for season in seasons:
    if month in seasons[season]:
        print(f"Время года: {season}")
