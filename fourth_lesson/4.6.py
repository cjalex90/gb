import itertools


def count_iter():
    for i in itertools.count(3):
        if i == 10:
            break
        yield i


def cycle_iter():
    mylist = [1, 2, 3]
    count = 0
    for i in itertools.cycle(mylist):
        if count == 10:
            break
        count += 1
        yield i
