class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        if not isinstance(self, Rectangle):
            return NotImplemented
        return self.width * self.height

    def __add__(self, other):
        if not isinstance(self, Rectangle):
            return NotImplemented
        return self.width * self.height + other.width * other.height

    def __mul__(self, n):
        if not isinstance(self, Rectangle):
            return NotImplemented
        return self.width * self.height * n

    def __eq__(self, other):
        if not isinstance(self, Rectangle):
            return NotImplemented
        return self.width * self.height == other.width * other.height

    def __gt__(self, other):
        if not isinstance(self, Rectangle):
            return NotImplemented
        return self.width * self.height > other.width * other.height

    def __lt__(self, other):
        if not isinstance(self, Rectangle):
            return NotImplemented
        return self.width * self.height < other.width * other.height

    def __str__(self):
        return f'{self.width} x {self.height}'


rectangle_1 = Rectangle(10, 20)
rectangle_2 = Rectangle(10, 20)
n = 15

print('rectangle_1 == rectangle_2: ', rectangle_1 == rectangle_2)
print('rectangle_1 != rectangle_2: ', rectangle_1 != rectangle_2)
print('rectangle_1 < rectangle_2: ', rectangle_1 < rectangle_2)
print('rectangle_1 > rectangle_2: ', rectangle_1 > rectangle_2)
print('rectangle_1: ', rectangle_1)
print('rectangle_2: ', rectangle_2)
print('Area rectangle_1 is:', rectangle_1.area())
print('Area rectangle_2 is:', rectangle_2.area())
print('Area rectangle_1 + rectangle_2 is:', rectangle_1 + rectangle_2)
print(f'Area rectangle * {n} is: ', rectangle_1.__mul__(n))
print()
