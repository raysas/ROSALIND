'''Bioinfotmatics Stronghold
Complementing a Strand of DNA'''

'''Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.'''

def Complementing(sequence):
    new_DNA_seq=''
    complement={'A':'T','T':'A','C':'G','G':'C'}
    for nuc in sequence:
        new_DNA_seq=complement[nuc]+new_DNA_seq
    return new_DNA_seq

str=input('enter DNA sequence:')
print(Complementing(str))
