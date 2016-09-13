'''
Pathogenicity islands are often marked by different GC content
than the rest of the genome. We will try to locate the pathogenicity island(s)
in our section of the Salmonella genome by computing GC content.
a) Write a function that divides a sequence into blocks and computes
the GC content for each block, returning a tuple. The function signature should look like
gc_blocks(seq, block_size)

To be clear, if seq = 'ATGACTACGT and block_size = 4, the blocks to be considered are
ATGA
CTAC

and the function should return (0.25, 0.5). Note that the blocks are non-overlapping
and that we don't bother with the end of the sequence that does not fit completely in a block.
b) Write a function that takes as input a sequence, block size, and a threshold GC content,
and returns the original sequence where every base in a block with GC content
above threshold is capitalized and every base in a block below the threshold is lowercase.
You would call the function like this:
mapped_seq = gc_map(seq, block_size, gc_thresh)

For example,
gc_map('ATGACTACGT', 4, 0.4)

returns 'atgaCTAC'. Note that bases not included in GC blocks are truncated.
c) Use the gc_map() function to generate a GC content map for the Salmonella
sequence with block_size = 1000 and gc_thresh = 0.45. Where do you think the pathogenicity island is?
d) Write the GC-mapped sequence (with upper and lower characters) to a new FASTA file.
Use the same description line (which began with a > in the original FASTA file) and
have line breaks every 60 characters in the sequence.'''

'''
a) Write a function that divides a sequence into blocks and computes
the GC content for each block, returning a tuple. The function signature should look like
gc_blocks(seq, block_size)

To be clear, if seq = 'ATGACTACGT and block_size = 4, the blocks to be considered are
ATGA
CTAC

and the function should return (0.25, 0.5). Note that the blocks are non-overlapping
and that we don't bother with the end of the sequence that does not fit completely in a block.'''

import parse_fasta
import dnatogc
import os

def get_gc(seq):
    '''return the GC content of a DNA sequence'''

    # Make sure all bases are capital
    capital_seq = seq.upper()

    # Calculate and return GC content
    return (seq.count('G') + seq.count('C')) / len(seq)

def get_blocks(seq, block_size):
    '''Given a sequence and block size, divide the sequence up into the blocks
    corresponding to the block size'''

    # Make sure block_size is less than sequence length
    if block_size > len(seq):
        raise RuntimeError('Block size of ' + block_size + ' is too large for the sequence')

    # Initialize list for blocks
    blocks = []

    # Find greatest number of whole blocks in sequence and get them
    for i in range(len(seq) // block_size):

        # Get block start index
        start = i * block_size

        # Get block stop index + 1
        stop = (i + 1) * block_size

        # Get block
        block = seq[start:stop]

        blocks.append(block)

    return blocks


def gc_blocks(seq, block_size):
    '''Given a sequence and block size, divide the sequence up into the blocks
    corresponding to the block size and return a tuple with the GC content for each block'''

    # Get the blocks
    blocks = get_blocks(seq, block_size)

    # Convert sequences to GC content
    gc_list = map(get_gc, blocks)

    return tuple(gc_list)

def gc_map(seq, block_size, gc_thresh):
    '''Given a sequence and block size, capitalize all of the sequence blocks
    that have a GC content above the threshold'''

    capital_seq = seq.upper()

    # Get the blocks
    blocks = get_blocks(capital_seq, block_size)

    # Convert sequences to GC content
    gc_list = map(get_gc, blocks)

    # Convert all blocks below the threshold to lower case
    for i, val in enumerate(gc_list):

        if not val >= gc_thresh:
            blocks[i] = blocks[i].lower()

    # Join all blocks back into main string
    final_sequence = ''.join(blocks)

    return final_sequence

def gc_map_write(infile, outfile, block_size, gc_thresh):

    # Get sequence from fasta file
    sequence, title = parse_fasta.parse_fasta(infile)

    # Get the final sequence
    final_sequence = gc_map(sequence, block_size, gc_thresh)

    # Initialize an array for creating sequence lines with title at front
    seq_lines = [title]

    for i in range(len(final_sequence) // 60 + 1):

        # Get line start index
        start = i * 60

        # Get line stop index + 1
        stop = (i + 1) * 60

        # Get line
        line = final_sequence[start:stop]

        seq_lines.append(line)

    # Add new lines
    seq_lines_final = map(lambda x: x + os.linesep, seq_lines)

    # Open the output file
    with open(outfile, 'w') as f:

        # Write the lines
        f.writelines(seq_lines_final)

    print('We have completed the operation. File is located at ' + outfile)
