def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculate the Hamming Distance between two DNA strands.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('DNA strand lengths do not match.')
    pairs = zip(strand_a.lower(), strand_b.lower())
    return sum([ch1 != ch2 for ch1, ch2 in pairs])
