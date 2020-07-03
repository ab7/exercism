def find_anagrams(word, candidates):
    word_chars = sorted([char.lower() for char in word])
    anagrams = []
    for _word in candidates:
        if _word.lower() == word.lower():
            continue
        chars = sorted([char.lower() for char in _word])
        if chars == word_chars:
            anagrams.append(_word)
    return anagrams
