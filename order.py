import product
import customer


class Order:
    """Create a order"""
    def __init__(self, customer, product):
        self.customer = customer
        self.product = product
        self.basket = 0  # кошик порожній

    def buy(self):
        pass

    def create_order(self):
        pass

    def read_basket(self):
        """How many items in the basket"""
        print(f"У кошику {self.basket} товарів")

    def update_basket(self, number_of_products):
        """Add products in basket"""
        self.basket = number_of_products

    def __str__(self):
        pass
