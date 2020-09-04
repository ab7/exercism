scores = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}


def score(word):
    scores_expanded = {char: score for key, score in scores.items() for char in key}
    return sum(scores_expanded[char] for char in word.upper())
