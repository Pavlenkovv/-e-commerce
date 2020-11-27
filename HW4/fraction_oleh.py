from math import gcd


class Rational:

    def __init__(self, a, b):
        if not isinstance(a, int):
            raise TypeError('a')
        if not isinstance(b, int):
            raise TypeError('b')
        if b == 0:
            raise ZeroDivisionError()

        self.__a, self.__b = a, b

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('other')

        b = self.__b * other.__b
        a = self.__a * other.__b + self.__b * other.__a
        return Rational(a, b)

    def __str__(self):
        tmp = gcd(self.__a, self.__b)
        self.__a, self.__b = self.__a // tmp, self.__b // tmp

        if abs(self.__a) > abs(self.__b):
            part1 = self.a // self.b
            part2 = self.a % self.b
            return f'{part1}({part2} / {self.b})'
        elif abs(self.a) == abs(self.b):
            return f'1'
        else:
            return f'{self.a} / {self.b}'


x1 = Rational(1, 2)
x2 = Rational(2, 2)

c = x1 + x2

print(x1, x2, c, sep='; ')