a = int(input("Введите количество км. за первый день: "))
b = int(input("Введите ожидаемое количество км.: "))

multiplier = 0.10  # 10%
days_count = 1
while a < b:
    days_count += 1
    a += a * multiplier

print(
    f"На {days_count} день спортсмен достиг результата — не менее {int(a)} км."
)
