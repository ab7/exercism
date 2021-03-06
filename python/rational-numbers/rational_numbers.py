from fractions import Fraction


class Rational:
    def __init__(self, numer, denom):
        numer, denom = self._reduce_fraction(numer, denom)
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return self.__class__(*self._reduce_fraction(numer, denom))

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return self.__class__(*self._reduce_fraction(numer, denom))

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return self.__class__(*self._reduce_fraction(numer, denom))

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return self.__class__(*self._reduce_fraction(numer, denom))

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return self.__class__(*self._reduce_fraction(numer, denom))

    def __pow__(self, power):
        numer = self.numer ** abs(power)
        denom = self.denom ** abs(power)
        return self.__class__(*self._reduce_fraction(numer, denom))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    @staticmethod
    def _reduce_fraction(numer, denom):
        reduced = Fraction(numer, denom)
        return reduced.numerator, reduced.denominator
