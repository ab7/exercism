def is_isogram(string: str) -> bool:
    letters = set()
    for char in string.lower():
        if char.isalpha():
            if char in letters:
                return False
            letters.add(char)
    return True
