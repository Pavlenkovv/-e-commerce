def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


print('fib(996) =', fib(996))
