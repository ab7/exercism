def is_valid(isbn: str) -> bool:
    """
    Determine if provided string is a valid ISBN-10 number.
    """
    total = 0
    mult = 10
    for char in isbn:
        if ord('0') <= ord(char) <= ord('9'):
            total += int(char) * mult
        elif mult == 1 and char.lower() == 'x':
            total += 10 * mult
        elif char != '-':
            return False
        else:
            continue
        mult -= 1
    return mult == 0 and total % 11 == 0


