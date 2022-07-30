'''
Bioinformatics Stronghold
Identifying unknown DNA

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. 
A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each)
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string
'''
def readFASTA(filename):
    #str-->{} takes a string of the filename and returns a dictionary of keys >rosalind#### and values the dna strand of each
    my_file=open(filename,'r')
    data={}
    dna, code='',''
    for line in my_file:
        if line.startswith('>'):
            #if this line is >rosalind#### format, save it as code and reset your dna strand
            if code!='':#if code is not empty, meaning you already saved a code, add it to its corresponding dna to 
                data[code]=dna
                dna=''
            code=line.strip()
        else: #if it's a dna segment, adss up to the strand
            dna+=line.strip()
    data[code]=dna #saves the last dna strand at the end of the loop
    return data

def computeGC(dna_strand):
    #str-->str takes a dna strand and computes it's gc content, returns it as a formatted string
    gc_count=dna_strand.count('C')+dna_strand.count('G')
    gc_percent=gc_count*100/len(dna_strand)
    return '%.6f' % gc_percent

def findMax(my_list):
    #{}-->int takes a list and returns the index of the highest value found
    max_index=0
    for i in range(len(my_list)):
        if my_list[i]>my_list[max_index]:
            max_index=i
    return max_index

def main():
    data=readFASTA('rosalind_gc.txt')
    gc_values=[]
    for key in data:
        gc=computeGC(data[key])#computes the gc of the dna strand found as value in each key in the dict
        gc_values.append(gc)
    index=findMax(gc_values)#get the index of the maximum value in the gc_values[]
    #this index corresponds respectively to each dna strand in the ddictionary
    my_key=list(data.keys())[index]
    my_value=gc_values[index]
    print(my_key,my_value,sep='\n')

main()
