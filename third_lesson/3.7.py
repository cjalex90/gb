import string


def int_func(word: str):
    if word.islower() and False not in list(map(lambda l: True if l in string.ascii_lowercase else False, word)):
        return word.title()


print(" ".join(list(map(int_func, input("Введите слова, разделенные пробелами: ").split(" ")))))
