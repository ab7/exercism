def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculate the Hamming Distance between two DNA strands.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('DNA strand lengths do not match.')
    ham = 0
    for i in range(len(strand_a)):
        if strand_a[i].lower() != strand_b[i].lower():
            ham += 1
    return ham
