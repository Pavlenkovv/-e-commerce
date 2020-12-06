import timeit


def memory():
    cache = {1: 1, 2: 1}

    def fibonacci(n):
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


print(memory()(900))
print(timeit.timeit(memory))
