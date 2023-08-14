#!/bin/env/python
'''
Data formats

Given: A collection of GenBank entry IDs.
Return: The shortest of the strings associated with the IDs in FASTA format.

'''
#imports
import Bio.Entrez
import Bio.SeqIO

#helper function 
def process_input(input_str):
    '''Takes a string of several IDs separated by spaces and returns them as a list of one string separated by commas.'''
    id_list = input_str.split()
    new_str = ", ".join(id_list)
    out=[new_str]
    return out

#accessing the genbank entries from IDs
def get_entries(id):
    '''takes genbank ids and returns the entry/ies associated with it(them)'''
    id=process_input(id)
    handle=Bio.Entrez.efetch(db="nucleotide", id=id, rettype="fasta")
    record=list(Bio.SeqIO.parse(handle, "fasta"))
    return record

def get_shortest_entry(records):
    '''takes a list of records and returns the shortest record's id'''
    shortest_record=records[0]
    for record in records:
        if len(record.seq) < len(shortest_record.seq):
            shortest_record=record
    return shortest_record.id

def get_fasta(entry_id):
    '''takes one genbank entry id and returns it in fasta format (also create a fasta file containing the info)'''
    handle=Bio.Entrez.efetch(db="nucleotide", id=entry_id, rettype="fasta")
    record=handle.read()
    with open(f"{entry_id}.fasta",'w') as fasta_file:
        fasta_file.write(record)
    return record

def main():
    print("-----------------------------")
    Bio.Entrez.email=input("enter yor email to access NCBI:")
    #1st we get the list of records from the ids given by input
    input_ids=input("Enter the genbank ids separated by a space: ")
    print("-----------------------------\n")
    entries=get_entries(input_ids)
    print("-----------1 done------------\n")
    #2nd we get the shortest record's id
    my_entry_id=get_shortest_entry(entries)
    print("-----------2 done------------\n")
    #finally, get the fasta format of the shortest record from its id
    my_fasta=get_fasta(my_entry_id)
    print("-----------output:-----------\n")
    print(my_fasta)
    print("-----------------------------")

if __name__=='__main__':
    main()
    # Path: FRMT.py will be used to run the program