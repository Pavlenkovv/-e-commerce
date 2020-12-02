import math


def prime(stop):
    if type(stop) != int:
        raise ValueError('Only int')
    if stop < 2:
        raise ValueError('Must be grater than 1')

    start = 2
    while start <= stop:
        isprime = True
        for x in range(2, int(math.sqrt(start) + 1)):
            if start % x == 0:
                isprime = False
                break
        if isprime:
            yield start
        start += 1


pr = prime(55)

for item in pr:
    print(item)
