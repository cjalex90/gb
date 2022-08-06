def my_func(x, y, z):
    mylist = [x, y, z]
    mylist.remove(min(mylist))
    return sum(mylist)


print(my_func(1, 2, 3))
