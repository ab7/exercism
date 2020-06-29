class Matrix:
    """Matrix implements utility methods for parsing a matrix string.

    The initialized matrix string is assumed to have rows delimited by the Unix
    style newline character and columns delimited by the space character.
    """

    def __init__(self, matrix_string: str,
                 row_delimiter: str = ' ',
                 col_delimiter: str = '\n') -> None:
        self.row_delimiter = row_delimiter
        self.col_delimiter = col_delimiter
        self.rows = self.matrix_string.split(self.row_delimiter)

    @staticmethod
    def convert_list_type(items: list, item_type: type) -> list:
        """Convert a list of items to provided type."""
        return [item_type(item) for item in items]

    def row(self, index: int) -> list:
        """Return row as list of integers at given index."""
        row = self.rows[index - 1].split(self.col_delimiter)
        return self.convert_list_type(row, int)

    def column(self, index: int) -> list:
        """Return column as list of integers at given index."""
        column_list = []
        for row in self.rows:
            row = row.split(self.col_delimiter)
            column_list.append(row[index - 1])
        return self.convert_list_type(column_list, int)
