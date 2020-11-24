class Circle:
    def __init__(self, rad):
        if not isinstance(rad, int):
            self.rad = rad
        else:
            raise TypeError

    def __eq__(self, other):
        return self.rad == other.rad

    def __gt__(self, other):
        return self.rad > other.rad

    def __lt__(self, other):
        return self.rad < other.rad


circle1 = Circle(55)
circle2 = Circle(55)

print(circle1 == circle1)
