def square(number: int) -> int:
    """Return value for number in geometric series.

    The input must be a valid integer representing a square on a chess board.
    There are 64 squares on a chess board.
    """
    if number < 1 or number > 64:
        raise ValueError('Input does not represent a valid chess square.')
    return 2 ** (number - 1)


def total() -> int:
    """Return geometric series sum based on number of chess squares (64)."""
    return sum(square(i) for i in range(1, 65))
