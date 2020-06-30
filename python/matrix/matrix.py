class Matrix:
    """Matrix implements utility methods for parsing a matrix string.

    The initialized matrix string is assumed to have rows delimited by the Unix
    style newline character and columns delimited by the space character.
    """

    def __init__(self, matrix_string: str) -> None:
        rows = matrix_string.splitlines()
        self.matrix = [[int(num) for num in row.split()] for row in rows]

    def row(self, index: int) -> list:
        """Return row as list of integers at given index."""
        return self.matrix[index - 1]

    def column(self, index: int) -> list:
        """Return column as list of integers at given index."""
        return [row[index - 1] for row in self.matrix]
