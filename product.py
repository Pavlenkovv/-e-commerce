import uuid

class Product:
    """Create a product"""
    def __init__(self, title, price):
        self.id = uuid.uuid4()
        self.price = price
        self.title = title
        # self.weight = weight

    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}, Price: {self.price} грн.'
