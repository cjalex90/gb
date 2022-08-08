def fact(n):
    count = 1
    factorial = 1
    for _ in range(n):
        factorial *= count
        yield factorial
        count += 1


for el in fact(4):
    print(el)
