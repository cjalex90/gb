file_name = "5.5_result.txt"
numbers = [str(i) for i in range(21)]

with open(file_name, "w", encoding="utf-8") as f:
    f.write(" ".join(numbers))
with open(file_name, "r", encoding="utf-8") as f:
    print(f"Сумма чисел из файла: {sum([int(i) for i in f.read().split()])}")
