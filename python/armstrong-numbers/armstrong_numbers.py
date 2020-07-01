def is_armstrong_number(number: int) -> bool:
    """Determine if given integer is an Armstrong number.

    An Armstrong number is a number that is the sum of its
    own digits each raised to the power of the number of digits.

    See https://en.wikipedia.org/wiki/Narcissistic_number.
    """
    result = 0
    num_str = str(number)
    for i in num_str:
        result += int(i) ** len(num_str)
    return result == number
