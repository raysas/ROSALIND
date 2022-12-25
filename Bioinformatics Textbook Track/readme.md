## Bioinformatics Algorithms: An Active Learning Approach

*2015 by Phillip Compeau and Pavel Pevzner. All rights reserved.*
Tested to be correct on the website before uploading, still trying to figure out the rest

### Chapter 1: Where in The DNA Does Replication Starts

**The biological problem:**

ok so replication starts at the origin of replication- called OriC in bacteria. How does it know the origin is the origin though? 
Protein DnaA scans through the whole genome until it finds a consensus sequence for the origin, then it calls for DnaC whcih brings whit it DnaB (or helicase) and hops in to create a replication bubble and proceed replication with the rest of the enzymes
Neat stuff (mind blowing lecture by dr roy✨)
Now what we're doing here:

**The computational problem:**

what we're trying to do throughout all the exercises is to eventually be capable to predict the OriC sequence for a small bacterium (*e.g., E. coli*).
The process starts by solving small computational problems which are the following:
- [Counting words problem](ba1a.py): takes a DNA string and a sequence and returns the number of occurences of this sequence in this DNA string
- [Frequent words problem](ba1b.py): takes a DNA string and a number k and returns all possible most frequent k-mers 
when looking for the origin of replication must find a region where there exist a k-mer of a sufficently large k that is unusually repeated (proba and stat wise).
(uses counting words as a subroutine to check how many times each k-mer is repeated to return only the max counted k-mer, not that efficient runs in $O(kn^2)$ could be reduced using a frequency list data structure)
- [Reverse pattern problem](ba1c.py): takes a DNA sequence and returns it's reverse complementary sequence. Useful to reduce the options of k-mers by checking the frequency of these sequences and their complements within the same region.
(could be the desired signal for DnaA)
- [Pattern matching problem](ba1d.py): takes a DNA string and a sequence and returns all the positions where this sequence is found starting by index 0 from the 1st bp.
This way we get to find whether the repitions of the k-mer are close or widely distributed throughout the genome.
