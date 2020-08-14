def score(word):
    result = 0
    for char in word:
        char_upper = char.upper()
        if char_upper in ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'):
            result += 1
        elif char_upper in ('D', 'G'):
            result += 2
        elif char_upper in ('B', 'C', 'M', 'P'):
            result += 3
        elif char_upper in ('F', 'H', 'V', 'W', 'Y'):
            result += 4
        elif char_upper in ('K'):
            result += 5
        elif char_upper in ('J', 'X'):
            result += 8
        elif char_upper in ('Q', 'Z'):
            result += 10
    return result
