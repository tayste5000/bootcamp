'''
a) Write a function, longest_orf(), that takes a DNA sequence as input
and finds the longest open reading frame (ORF) in the sequence
(we will not consider reverse complements).
A sequence fragment constitutes an ORF if the following are true.
It begins with ATG.
It ends with any of TGA, TAG, or TAA.
The total number of bases is a multiple of 3.
Note that the sequence ATG may appear in the middle of an ORF. So, for example,
GGATGATGATGTAAAAC

has two ORFs, ATGATGATGTAA and ATGATGTAA. You would return the first one,
since it is longer of these two.
Hint 1: The statement for this problem is a bit ambiguous as it is written.
What other specification might you need for this function?
Hint 2: You might need to check the documentation of different string methods,
like find() to see how to get the functionality you are looking for.
b) Use your function to find the longest ORF from the section of the Salmonella genome we are investigating.
c) Write a function that converts a DNA sequence into a protein sequence.
The dictionaries in the bioinfo_dicts module may be useful.
d) Translate the longest ORF you generated in part (b) and perform a BLAST search.
Search for the protein sequence (a blastp query). What gene is it?
e) [challenge] Modify your function to return the n longest ORFs.
Compute the five longest ORFs for the Salmonella genome section we are working with.
Perform BLAST searches on them. What are they?

1 is transcriptional regulator (WP_001120085.1)
2 is L-fucose isomerase (WP_000724126.1)
3 is Formate hydrogenlyase transcriptional activator
4 is DNA mismatch repair protein MutS
5 is two-component sensor histidine kinase BarA
'''
import parse_fasta
import bioinfo_dicts

def get_reading_frames(seq):
    '''Get the three possible forward orfs, divided into codons, from a sequence'''

    # Initialize a tuple for the RFs
    rf_list = ([], [], [])

    # Split into 3 RFs, then split each into anticodons
    for i in range(3):

        for j in range((len(seq) - i) // 3):
            # Get block start index
            start = j * 3

            # Get block stop index + 1
            stop = (j + 1) * 3

            rf_list[i].append(seq[i:][start:stop].upper())

    return rf_list

def get_longest_orf(seq, n):
    '''Get the longest orf from a sequence'''

    # Get rfs
    rf_list = get_reading_frames(seq)

    # Initialize temporary ORF holder
    temp_orf = []

    # Initialize longest ORF holder
    orfs = []

    for rf in rf_list:

        for codon in rf:

            # If orf has come to an end
            if bioinfo_dicts.codons[codon] == '*':

                # Add to orfs list
                orfs.append(temp_orf)

                # Reset counter and temp_orf
                temp_orf = []

            else:

                # Add codon to temp_orf
                temp_orf.append(codon)

    # This should sort by length
    orfs.sort(key=lambda x: len(x))

    # Get N longest orf's and join codons
    orfs = map(lambda x: ''.join(x), orfs[-1 * n:])

    return

def dna_to_protein(seq):

    protein = ''

    for i in range(len(seq) // 3):

        # Get codon start index
        start = i * 3

        # Get codon stop index + 1
        stop = (i + 1) * 3

        codon = seq[start:stop]

        protein += bioinfo_dicts.codons[codon]

    return protein
