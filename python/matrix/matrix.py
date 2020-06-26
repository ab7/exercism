from typing import List


class Matrix:
    """Matrix implements utiliy methods for parsing a matrix string.

    The initialized matrix string is assumed to have rows delimited by the Unix
    style newline character and columns delimited by the space character.
    """

    Row = List[int]
    Rows = List[Row]
    Column = List[int]

    def __init__(self, matrix_string: str) -> None:
        self.matrix_string = matrix_string

    def _converted_matrix(self) -> Rows:
        """Convert a matrix string to a list using provided delimiters."""
        return [[int(c) for c in r.split()] for r in self.matrix_string.split('\n')]

    def row(self, index: int) -> Row:
        """Return a Row by index using converted matrix string."""
        return self._converted_matrix()[index - 1]

    def column(self, index: int) -> Column:
        """Return a Column by index using converted matrix string."""
        return [row[index - 1] for row in self._converted_matrix()]
