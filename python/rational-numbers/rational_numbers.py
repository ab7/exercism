from fractions import Fraction


class Rational:
    def __init__(self, numer, denom):
        reduced = Fraction(numer, denom)
        self.numer = reduced.numerator
        self.denom = reduced.denominator

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        reduced = Fraction(numer, denom)
        self.numer = reduced.numerator
        self.denom = reduced.denominator
        return self

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        reduced = Fraction(numer, denom)
        self.numer = reduced.numerator
        self.denom = reduced.denominator
        return self

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        reduced = Fraction(numer, denom)
        self.numer = reduced.numerator
        self.denom = reduced.denominator
        return self

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        reduced = Fraction(numer, denom)
        self.numer = reduced.numerator
        self.denom = reduced.denominator
        return self

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        reduced = Fraction(numer, denom)
        self.numer = reduced.numerator
        self.denom = reduced.denominator
        return self

    def __pow__(self, power):
        numer = self.numer ** abs(power)
        denom = self.denom ** abs(power)
        reduced = Fraction(numer, denom)
        self.numer = reduced.numerator
        self.denom = reduced.denominator
        return self

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
