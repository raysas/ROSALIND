'''Bioinformatics Stronghold
Transcribing DNA into RNA'''

'''
Given: A DNA string t having length at most 1000 nt
Return: The transcribed RNA string of t
'''
def Transcribing(sequence):
    RNA_seq=''
    complement={'A':'U','T':'A','C':'G','G':'C'}
    for nuc in sequence:
        RNA_seq+=complement[nuc]
    return RNA_seq

str=input('enter DNA sequence:')
print(Transcribing(str))
