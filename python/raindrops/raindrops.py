def convert(number: int) -> str:
    result = []
    if number % 3 == 0:
        result.append('Pling')
    if number % 5 == 0:
        result.append('Plang')
    if number % 7 == 0:
        result.append('Plong')
    if not result:
        return str(number)
    return ''.join(result)
