class Person:
    """Any Person"""

    def __init__(self, surname=None, name=None, age=None, *args, **kwargs):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f'Surname: {self.surname}, name: {self.name}, age: {self.age}'
