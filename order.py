class Order:
    """Create a order"""

    count = 0

    def __init__(self, customer=None):
        self.id = Order.count
        self.customer = customer
        self.basket = {}
        Order.count += 1

    def order_total(self):
        """calculation of the total cost"""
        total = 0
        for item in self.basket:
            total += item.price * self.basket[item]
        return total

    def add_product(self, product):
        if self.basket.get(product):
            self.basket[product] += 1
        else:
            self.basket[product] = 1

    def __str__(self):
        res = str(self.customer) + '\n'
        for item in self.basket:
            res += f'{item} \n\t {self.basket[item]} x {item.price} грн. = {item.price * self.basket[item]} грн.\n'
        return res