def my_func(x, y):
    if x > 0 > y:
        result = x
        for i in range(abs(y) + 1):  # or range((-y) + 1)
            result /= x
        print(result)

    else:
        print("Требуется ввести положительное число x и целое отрицательное число y")


my_func(2, -3)
