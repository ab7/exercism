from heapq import heapify, heappop


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


def personal_top_three(scores: list) -> list:
    """
    Return top three scores from score collection.
    """
    scores_inverted = [~score for score in scores]
    heapify(scores_inverted)
    return [~heappop(scores_inverted) for _ in range(min(len(scores), 3))]
