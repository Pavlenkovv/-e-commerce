class Customer:
    """Create a customer"""
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{id(self), self.name, self.surname, self.phone}'
