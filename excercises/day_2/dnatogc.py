def complement_base(base, material):
    '''Return the watson-crick complement of a base'''

    # Return complementary bases depending on which string the base matches
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        if material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Cc':
        return 'G'
    elif base in 'Gg':
        return 'C'
    else:
        raise Exception('This is not a valid base')

def reverse_complement(sequence, material='DNA'):
    '''Compute the reverse complement of a nucleic acid sequence WITHOUT USING THE REVERSED ITERATOR MODIFYING FUNCTION'''

    # Initialize empty string
    complement = ''

    # Iterate for each base sequence
    for base in sequence:

        # Add complement base TO THE FRONT
        complement = complement_base(base, material) + complement

    return complement
