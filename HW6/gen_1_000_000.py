from random import randint
from timeit import timeit

# with open('1_000_000.txt', 'w') as file:
#     for i in range(1_000_000):
#         file.write(f' {randint(0, 1000)} \n')

s = """\
f = open('1_000_000.txt', 'r')
my_sum = 0
data = f.readlines()
for item in data:
    my_sum += int(item)
"""

print(timeit(s, number=20))

s = """\
f = open('1_000_000.txt', 'r')
my_sum = 0
for item in f:
    my_sum += int(item)
"""

print(timeit(s, number=20))

s = """\
f = open('1_000_000.txt', 'r')
gen_expr = (int(item) for item in f)
my_sum = sum(gen_expr)
my_sum = 0
"""

print(timeit(s, number=20))
