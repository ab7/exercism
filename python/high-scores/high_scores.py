def latest(scores: list) -> int:
    """
    Return the last added score from collection.
    """
    return scores[-1]


def personal_best(scores: list) -> int:
    """
    Return max score from score collection.
    """
    return max(scores)


def personal_top_three(scores):
    """
    Return top three scores from score collection.
    """
    top_three = scores[:3]
    for score in scores[3:]:
        for i, top in enumerate(top_three):
            if score > top:
                top_three[i] = score
                break
    return sorted(top_three, reverse=True)
