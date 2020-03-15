def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('not of equal length')
    errores     = [a!=b for a,b in zip(strand_a, strand_b)]
    return sum(errores)