'''
Finding a Motif in DNA
'''

def search(str, pattern):
    '''
    take a string str of a dna sequence and a string pattern of bp
    returns the location at which th epattern is found the the str sequence
    if no match is found returns an empty list
    '''
    match=[]
    for i in range(len(str)-len(pattern)):
        if str[i:i+len(pattern)]==pattern:
            match.append(i+1)
    printArray(match)
    return match

def printArray(arr):
    '''takes a list and prints its contents'''
    for i in arr:
        print(i,end=' ')

def readDataset(filename):
    # print('hi')
    f=open(filename,'r')
    DNA=f.readline()
    motif=f.readline()
    search(DNA, motif)

DNA='GATATATGCATATACTT'
motif='ATAT'

readDataset('rosalind_subs.txt')

# print('out...')
