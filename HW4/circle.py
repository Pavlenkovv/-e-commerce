class Circle:
    def __init__(self, rad):
        if not isinstance(rad, int):
            raise TypeError('It`s not a number')
        self.rad = rad

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.rad == other.rad

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.rad > other.rad

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.rad < other.rad

    def __str__(self):
        return f'{self.rad}'


circle1 = Circle(65)
circle2 = Circle(55)

print(circle1 < circle1)
