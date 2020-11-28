class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "Goods [name = {}, price = {}]".format(self.name, self.price)


class Basket:
    def __init__(self, user):
        self.user = user
        self.goods_list = []

    def add_goods(self, goods):
        self.goods_list.append(goods)

    def __str__(self):
        result = "User: {}\n".format(self.user)

        for good111 in self.goods_list:
            result += str(good111) + "\n"
        return result

    def __iter__(self):
        return BasketIterator(self.goods_list)


class BasketIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


basket = Basket("Alexander_Ts")
a = Goods("Apple", 35)
b = Goods("Milk", 50)
basket.add_goods(a)
basket.add_goods(b)

for good in basket:
    print(good)
