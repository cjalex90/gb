while True:
    line = input("Введите текст для записи в файл: ")
    if line:
        with open("5.1_result.txt", "a", encoding="utf-8") as f:
            f.write(f"{line}\n")
    else:
        print("Текст записан в файл")
        break
