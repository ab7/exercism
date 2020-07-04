def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculate the Hamming Distance between two DNA strands.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('DNA strand lengths do not match.')
    pairs = zip(strand_a.lower(), strand_b.lower())
    return sum([1 for pair in pairs if pair[0] != pair[1]])
