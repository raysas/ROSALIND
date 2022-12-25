'''
Algorithmic Heights
Binary Search

The problem is to find a given set of keys in a given array.
Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from -105 to 105 and a list of m integers -105≤k1,k2,…,km≤105.
Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.
'''



def _BiSearch_(my_arr,k,s,e):
    #private helper method that takes a sorted array, a number k, start index s and end index e, returns the index of k in the array recursively
    if s>e:
        return -1
    else:
        m=(s+e)//2 #midlle index
        if int(my_arr[m])>int(k):
            return _BiSearch_(my_arr,k,s,m-1)
        elif int(my_arr[m])<int(k):
            return _BiSearch_(my_arr,k,m+1,e)
        return m

def BiSearch(my_arr, k):
    '''takes a sorted array of numbers and number k and returns the index of k if found, -1 if not'''
    return _BiSearch_(my_arr,int(k),0,len(my_arr)-1)


def readFile(filename):
    '''takes a filename found in the same working directory and returns it as an array of items each line of the file'''
    my_file=open(filename,'r')
    arr=[]
    for line in my_file:
        arr.append(line.strip("\n"))
    return arr

def main():
    inp=input('enter filename:')
    my_arr=readFile("datasets\\"+inp)#windows friendly
    size_arr=int(my_arr[0])
    size_k=int(my_arr[1])
    my_list=my_arr[2].split(" ")
    k_list=my_arr[3].split(" ")
    out=""
    for k in range(size_k):
        x=BiSearch(my_list,k_list[k])
        if x!=-1:
            x+=1
        out+=str(x)+" "
    output=open("datasets\\result.txt","w")
    output.write(out.strip(" "))


#the program prompts the user for a file name of the dataset containing the input form rosalind, taking for granted it's found in ROSALIND/datasets


main()


    