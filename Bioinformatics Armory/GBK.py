'''
Bioinfo Armory
GenBank

Given: A genus name, followed by two dates in YYYY/M/D format.
Return: The number of Nucleotide GenBank entries for the given genus 
    that were published between the dates specified.
'''
import Bio.Entrez

def get_genbank_entries(genus, start_date, end_date):
    '''takes a genus name, followed by two dates in YYYY/M/D format and returns the record of Nucleotide GenBank entries for the given genus that were published between the dates specified'''
    #accessing GenBank database using Entrez specifying "nucleaotide" as db
    #specifying the search term
    Bio.Entrez.email="rayane.s.adam@gmail.com"
    # To make use of NCBI's E-utilities, NCBI requires you to specify your email address with each request.
    handle= Bio.Entrez.esearch(db="nucleotide", term=f"{genus}[Organism] AND ({start_date}[Publication Date] : {end_date}[Publication Date])")
    record=Bio.Entrez.read(handle)
    print(f"the number of records is {record['Count']}") #prints the count for output
    return record

genus=input("Enter a genus name: ")
start_date=input("Enter a start date in YYYY/M/D format: ")
end_date=input("Enter an end date in YYYY/M/D format: ")
get_genbank_entries(genus, start_date, end_date)