import uuid


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
        return f'ID: {self.id}, Title: {self.title}, Price: {self.price} грн.'
