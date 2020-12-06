import math


def out(num32):
    mem_dict = {}
    if num32 in mem_dict:
        return mem_dict[num32]
    # else:
    #     mem_dict[num] = out(num)

    def inner(num):
        # nonlocal num
        if num < 0:
            print("Incorrect input")
            # First Fibonacci number is 0
        elif num == 1:
            return 0
        # Second Fibonacci number is 1
        elif num == 2:
            return 1
        else:
            return inner(num - 1) + inner(num - 2)
    return inner


fib = out(1)
print(fib(30))


# for i in fib:
#     print(i)
