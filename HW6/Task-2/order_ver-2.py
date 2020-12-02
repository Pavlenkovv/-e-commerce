import uuid  # for unique id


class Customer:
    """Create a customer"""
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{id(self), self.name, self.surname, self.phone}'


class Product:
    """Create a product"""
    def __init__(self, title):
        self.id = uuid.uuid4()
        self.title = title

        try:
            self.price = int(input(f"Please enter the price for {self.title}: "))
            if not isinstance(self.price, (int, float)) or self.price < 0:
                raise RuntimeError("The price of the goods must be positive number")
        except (TypeError, ValueError) as error:
            raise error("The price of the goods must be positive number")

    def __str__(self):
        return f'Title: {self.title}, Price: {self.price} грн'


class Order:
    """Create a order"""

    count = 0

    def __init__(self, customer=None):
        self.id = Order.count
        self.customer = customer
        self.basket = []
        Order.count += 1

    def order_total(self):
        """calculation of the total cost"""
        total = 0
        for item in self.basket:
            total += item.price * self.basket[item]
        return total

    def add_product(self, product):
        self.basket.append(product)

    def __str__(self):
        result = str(self.customer) + '\n'

        for prod_in_basket in self.basket:
            result += str(prod_in_basket) + "\n"
        return result

    def __iter__(self):
        return OrderIterator(self.basket)


class OrderIterator:
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


if __name__ == '__main__':
    try:
        product1 = Product("Apple")
        product2 = Product("Cherry")
    except (TypeError, ValueError) as err:
        print(err)

    client1 = Customer('Ira', 'Pavlenko', '+38 097 1111111')
    client2 = Customer('Roma', 'Ivaniuk', '+38 097 2222222')

    order_1 = Order(client1)
    order_1.add_product(product1)
    order_1.add_product(product2)
    print('ORDER')

    for i in order_1:
        print(i)

    order_2 = Order(client2)
    order_2.add_product(product1)
    order_2.add_product(product1)
    order_2.add_product(product1)
    order_2.add_product(product1)
    order_2.add_product(product1)
    order_2.add_product(product2)
    order_2.add_product(product2)

    print('= ' * 15)
    print('ORDER:')
    for i in order_2:
        print(i)
