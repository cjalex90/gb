translate = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("5.4_source.txt", "r", encoding="utf-8") as f:
    numbers = [n.rstrip().split() for n in f.readlines()]
    for name, dash, num in numbers:
        with open("5.4_result.txt", "a", encoding="utf-8") as f:
            f.write(f"{translate[name]} {dash} {num}\n")
