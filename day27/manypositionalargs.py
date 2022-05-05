def add(*args):
    for n in args:
        print(n)


add(3, 5, 7, 8)


def add_nums(*args):
    add_up = 0
    for n in args:
        add_up += n
    return add_up


sum_of_nums = add_nums(2, 4, 6)

print(sum_of_nums)
