'''Bioinformatics Stronghold
Counting DNA nucleotides'''

'''
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
'''
def nucleotides_count(sequence):
    A_count=0
    T_count=0
    C_count=0
    G_count=0
    for nuc in sequence:
        if nuc=='A':
            A_count+=1
        elif nuc=='T':
            T_count+=1
        elif nuc=='C':
            C_count+=1
        else:
            G_count+=1
    return A_count, C_count, G_count, T_count

str=input('Enter DNA sequence:')
print(nucleotides_count(str))