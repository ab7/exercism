def square_of_sum(number: int) -> int:
    """Return sum of first N natural numbers squared.

    This algorithm is based on Faulhaber's formula.
    """
    return ((number * (number + 1)) / 2) ** 2


def sum_of_squares(number: int) -> int:
    """Return sum of the squares of the first N natural numbers.

    This algorithm is based on Faulhaber's formula.
    """
    return (number * (number + 1) * (2 * number + 1)) / 6


def difference_of_squares(number: int) -> int:
    """Return the difference bewteen square of the sum and the sum of the squares."""
    return square_of_sum(number) - sum_of_squares(number)
