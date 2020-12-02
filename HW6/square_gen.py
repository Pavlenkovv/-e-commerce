def square_gen(n):
    i = 0
    exponent = 1
    while i <= n:
        temp_exponent = (yield i ** exponent)
        if temp_exponent is not None:
            exponent = temp_exponent
        i = i + 1


g = square_gen(153)
next(g)
print(g.send(2))
print(g.send(3))
print(g.send(5))
print(next(g))
