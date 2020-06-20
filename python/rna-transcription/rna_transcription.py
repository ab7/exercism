def to_rna(dna_strand: str) -> str:
    try:
        return ''.join([{
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U',
        }[n] for n in dna_strand])
    except KeyError:
        return 'Invalid DNA strand'
