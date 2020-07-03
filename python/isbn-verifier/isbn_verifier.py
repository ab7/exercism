def is_valid(isbn: str) -> bool:
    """
    Determine if provided string is a valid ISBN-10 number.

    A ISBN-10 number has exactly 9 digits plus a check number.
    The check number can be a digit [0-9] or the character 'X' which
    represents 10. To check validity each digit is multiplied by the
    count and summed with the previous digit. The remainder of the
    total sum of the 10 products divided by 11 should be 0.

    Dashes are valid as part of the ISBN and are ignored.
    """
    total = 0
    count = 10
    for char in isbn:
        if char.isdigit():
            total += int(char) * count
            count -= 1
        elif count == 1 and char.lower() == 'x':
            total += 10 * count
            count -= 1
        elif char != '-':
            return False
    return count == 0 and total % 11 == 0
