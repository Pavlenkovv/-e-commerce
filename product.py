class Product:
    """Create a product"""
    def __init__(self, name, price, description, weight):
        self.name = name
        self.price = price
        self.description = description
        self.weight = weight

    def __str__(self):
        return f'{id(self), self.name, self.description, self.price, self.weight}'
