import math
import random


class Fac:

    def __init__(self):
        self.mem_dict = {}

    def __call__(self, num, *args, **kwargs):
        if num in self.mem_dict:
            return self.mem_dict[num]
        else:
            self.mem_dict[num] = math.factorial(num)
            return math.factorial(num)


f = Fac()

for i in range(100):
    print(f(random.randint(0, 10)))
