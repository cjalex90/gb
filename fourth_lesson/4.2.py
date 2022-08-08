source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [el for idx, el in enumerate(source_list) if idx and el > source_list[idx - 1]]
print(my_list)
