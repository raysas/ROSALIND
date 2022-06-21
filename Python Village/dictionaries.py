'''Python village
6. Dictionaries'''

'''
Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''
str=input('enter a string:')
List=str.split()
dict={}
list1=[]
list_of_words=[]
for word in List:
    c=0
    if word in list_of_words:
        continue
    for term in List:
        if word==term:
            c+=1
    list1.append((word, c))
    list_of_words.append(word)
