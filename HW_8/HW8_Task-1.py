sequence = [2, 4, 5, 7, 44, 345, 1, 3, -8, -2112, -9, 88, 0, 6]


def gen_fuu(stop_n: int, predicate) -> int:
    for element in sequence:
        if element < stop_n:
            if predicate(element):
                yield element
    return


def custom_function(number:int) -> bool:
    return number > 0


g = gen_fuu(10, custom_function)

for item in g:
    if item > 6:
        g.close()
    print(item)
