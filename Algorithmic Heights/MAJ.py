'''Majority element: O(nlogn) solution'''

def __getMaj__(a,r,l,count,max_index):
    
   '''takes an array, right index, left index, index of the most repeated element
   returns a tupe of counts array which counts the occurence of each index and the index of the most counted'''
   if r==l:
        count[int(a[r])]+=1
        if count[max_index]<count[int(a[r])]:
            max_index=r
        return count, max_index
   else:
        mid=(r+l)//2
        count, max_index= __getMaj__(a,r,mid,count,max_index)
        count, max_index=__getMaj__(a,mid+1,l,count,max_index)
        return count, max_index

def getMaj(a):
    '''takes an array and the length of the counts array required i.e. the range of numbers 0..n of found in a where length=n
    returns the counts array after performing the majority element operation along with the index of the most repeated'''
    count=[0 for c in range(100000)]#sorry memory
    return __getMaj__(a,0,len(a)-1,count,0)

def solveMaj(a):
    '''takes an array of positive integers not exceeding 10^5.
    returns an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise''' 
    my_arr,ind=getMaj(a)
    print("%d is found %d times;"%(int(a[ind]),int(my_arr[ind])))
    if my_arr[ind]>len(a)/2:
        return a[ind]
    return -1

def main(filename):
    f=open(filename,'r')
    s=f.readline().split(" ")#first line has k and n respectively
    k=int(s[0])
    output=""
    for i in range(k):
        line=f.readline().strip()
        a=line.split(" ")
        output+=str(solveMaj(a))+" "
    print(output)
    return output.strip()

main("rosalind_maj.txt")