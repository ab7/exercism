def is_isogram(string: str) -> bool:
    chars = [char for char in string.lower() if char.isalpha()]
    return len(chars) == len(set(chars))
