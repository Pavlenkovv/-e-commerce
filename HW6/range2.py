def my_range(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError("Only int")

    if step == 0:
        raise ValueError("Step cannot be zero")

    try:
        start, stop, step = int(start), int(stop), int(step)
    except ValueError:
        raise ValueError('Only int')

    if stop > 0:
        while start < stop:
            yield start
            start += step
    elif stop < 0 and step < 0:
        while start > stop:
            yield start
            start -= abs(step)
    else:
        raise ValueError('Error')

    return None


for i in my_range(15, 50, 5):
    print(i)
