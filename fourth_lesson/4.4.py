source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
mylist = [i for i in source_list if source_list.count(i) == 1]
print(mylist)