def my_range(start=0, stop=None, step=1):
    start = 1
    stop = 2
    step = 1
    # index = 1
    while stop <= n:
        next_number = start + stop
        start = stop
        stop = next_number
        index = index + 1
        yield next_number
    return


# a = my_range(10)
for i in my_range(15):
    print(i)
