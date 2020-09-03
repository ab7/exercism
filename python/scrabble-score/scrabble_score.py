def score(word):
    result = 0
    for char in word.upper():
        if char in 'AEIOULNRST':
            result += 1
        elif char in 'DG':
            result += 2
        elif char in 'BCMP':
            result += 3
        elif char in 'FHVWY':
            result += 4
        elif char in 'K':
            result += 5
        elif char in 'JX':
            result += 8
        elif char in 'QZ':
            result += 10
    return result
