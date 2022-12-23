'''Python village
6. Dictionaries'''

'''
Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''


def main():
    my_dict={}
    str=input("enter a string:")
    for w in str.split(' '):
        if w in my_dict:
            my_dict[w]+=1
        else:
            my_dict[w]=1
    for key in my_dict.keys():
        print(key, my_dict[key])

main()
