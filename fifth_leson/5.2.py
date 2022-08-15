file_name = "5.2_result.txt"

with open(file_name, "a", encoding="utf-8") as f:
    f.writelines(
        list(map(lambda line: f"{line}\n", [
            "First line", "Second string", "Third row"
        ])))

with open(file_name, "r", encoding="utf-8") as f:
    text_list = f.readlines()
    line_count = len(text_list)
    word_count = len([w for w in "".join(text_list).split()])
    print(f"Подсчитано {line_count} строк и {word_count} слов")
