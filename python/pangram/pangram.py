def is_pangram(sentence: str) -> bool:
    char_set = set()
    for char in sentence:
        ascii_val = ord(char.lower())
        if ord('a') <= ascii_val <= ord('z'):
            char_set.add(ascii_val)
    return len(char_set) == 26
