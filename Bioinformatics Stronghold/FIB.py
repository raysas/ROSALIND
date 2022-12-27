'''Bioinformatics Stronghold
Rabbits and Recurrence Relations'''

'''
In 1202, Leonardo of Pisa (commonly known as Fibonacci) considered a mathematical exercise regarding the reproduction of a population of rabbits. He made the following simplifying assumptions about the population:

*The population begins in the first month with a pair of newborn rabbits.
*Rabbits reach reproductive age after one month.
*In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
*Exactly one month after two rabbits mate, they produce one male and one female rabbit.
*Rabbits never die or stop reproducing.

A sequence is an ordered collection of objects (usually numbers), 
which are allowed to repeat. 
Sequences can be finite or infinite. Two examples are the finite sequence (π,-2-√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). 
We use the notation an to represent the n-th term of a sequence.
A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. 
In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. 
A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. 
As a result, if Fn represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). 
Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.
When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. 
This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases

Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)
'''

#month 1: 1 pair
#month 2: 1 pair
#month 3: k+1 pairs      k new + 1 or k*U1+U2
#month 4: 2k+1 pairs     k new + k+1 
#month 5: k^2+3k+1 pairs k(k+1) new + 2k+1
#so here's the following seq: base case for n=1,2, Un=1
#induction step: k*Un-2 + Un-1


def rabbitsRecurrence(n,k):
    #takes number of months n and number of offspring k and returns the number of pairs of rabbits present after n months
    a=[0 for x in range(n+1)]
    a[0],a[1]=1,1
    for i in range(2,n+1):
        a[i]=k*a[i-2]+a[i-1]
    return a[n]

def main():
    num=eval(input("enter n:"))
    k_val=eval(input("enter k:"))
    print("rabbits recurrence value for n=%d and k=%d is %d" %(num,k_val,rabbitsRecurrence(num,k_val)))

main()