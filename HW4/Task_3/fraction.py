"""Создайте класс «Правильная дробь» и реализуйте методы сравнения,
сложения, вычитания и произведения для экземпляров этого класса."""

from math import gcd


class Fraction:

    def __init__(self, a, b):
        if not isinstance(a, int):
            raise TypeError('a')
        if not isinstance(b, int):
            raise TypeError('b')
        if b == 0:
            raise ZeroDivisionError()
        self.a, self.b = a, b

    def __add__(self, other):
        if not isinstance((self or other), Fraction):
            return NotImplemented
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Fraction(a, b)

    def __sub__(self, other):
        if not isinstance((self or other), Fraction):
            return NotImplemented
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        return Fraction(a, b)

    def __mul__(self, other):
        if not isinstance((self or other), Fraction):
            return NotImplemented
        a = self.a * other.a
        b = self.b * other.b
        return Fraction(a, b)

    def __truediv__(self, other):
        if not isinstance((self or other), Fraction):
            return NotImplemented
        elif other.b == 0:
            raise ZeroDivisionError()
        a = self.a * other.b
        b = self.b * other.a
        return Fraction(a, b)

    def __str__(self):
        nod = gcd(self.a, self.b)
        self.a, self.b = self.a // nod, self.b // nod
        if abs(self.a) > abs(self.b):
            part1 = self.a // self.b
            part2 = self.a % self.b
            return f'{part1}({part2}/{self.b})'
        elif abs(self.a) == abs(self.b):
            return f'1'
        else:
            return f'{self.a}/{self.b}'
        # return f'{self.a}/{self.b}'


x1 = Fraction(1, 2)
x2 = Fraction(3, 4)
c = x1 + x2

print(x1, x2, c, sep='; ')
