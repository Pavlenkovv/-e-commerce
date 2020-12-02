def geo(start, stop):
    if type(stop) != int:
        raise ValueError('Only int')
    mn = start
    while start <= stop:
        yield start
        start *= mn


g = geo(2, 500)

for i in g:
    if i > 100:
        g.close()
    print(i)

