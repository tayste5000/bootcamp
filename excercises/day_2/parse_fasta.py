'''
There are packages, like Biopython and scikit-bio for processing files you encounter in bioinformatics.
In this problem, though, we will work on our file I/O skills.
a) Use command line tools to investigate the FASTA file.
You will notice that the first line begins with a >,
signifying that the line contains information about the sequence.
The remainder of the lines are the sequence itself.
b) Use the file I/O skill you have learned to read in the sequence
and store it as a single string with no gaps.
'''
import os

def parse_fasta(file_name):
    '''Take a filename corresponding to a fasta sequence and
    return the full sequence as string'''

    # Make sure it is a file
    if not (os.path.isfile(file_name)):
        raise RuntimeError(file_name + ' is not a valid file name.')

    # Initialize actual_sequence array
    lines = []

    with open(file_name) as f:

        lines = f.readlines()

    # Get FASTA header, kinda cheating by assuming where the header is
    title = lines[0].replace(os.linesep, '')

    # Remove lines with '>'
    actual_sequence = filter(lambda x: x[0] != '>', lines)

    # Remove \n
    cleaned_sequence = map(lambda x: x.replace(os.linesep, ''), actual_sequence)

    # Join into single string
    final_sequence = ''.join(cleaned_sequence)

    return (final_sequence, title)
