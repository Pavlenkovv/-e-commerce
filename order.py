import product
import customer


class Order:
    """Create a order"""
    def __init__(self, customer, product):
        self.customer = customer
        self.products = []
        self.products.append(product)
        self.total_cost = 0

    def update_order(self, product):
        """Add products in order"""
        self.products.append(product)

    def total_cost(self, products):
        """calculation of the total cost"""
        for i in self.products:
            self.total_cost += self.products[i]

    def __str__(self):
        return f'{self.customer} {self.products}, Total cost: {self.total_cost}'
