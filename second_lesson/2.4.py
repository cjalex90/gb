text = input("Введите несколько слов через пробел: ")

for number, word in enumerate(text.split(), 1):
    if len(word) > 10:
        word = word[:10] + "..."
    print(f"{number}: {word}")
