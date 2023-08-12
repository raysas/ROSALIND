'''
Bioinformatics Armory:
Intro 

Given: A DNA string s of length at most 1000 bp.
Return: Four integers (separated by spaces) 
    representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' 
    occur in s

Using BioPython
Note: You must provide your answer in the format shown in the sample output below.
'''

import Bio.Seq #pip install biopython

def counting_nuc(dna_string):
    '''takes a DNA string and returns the number of times that the symbols 'A', 'C', 'G', and 'T' occur in it'''
    s=Bio.Seq.Seq(dna_string)
    a=s.count('A');t=s.count('T');g=s.count('G');c=s.count('C')
    print(f"{a} {c} {g} {t}")
    return a,c,g,t
    
s=input("Enter a DNA string: ")
counting_nuc(s)