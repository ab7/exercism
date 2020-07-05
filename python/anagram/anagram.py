def find_anagrams(word: str, candidates: list) -> list:
    filtered = [w for w in candidates if w.lower() != word.lower()]
    return [w for w in filtered if sorted(word.lower()) == sorted(w.lower())]
