x = 10
lst2 = []
lst = (x ** 3 for x in range(2, x))

for i in lst:
    lst2.append(i)

print(lst2)
