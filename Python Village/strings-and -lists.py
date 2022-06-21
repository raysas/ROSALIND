'''Python Village
3. Strings and Lists'''

'''Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.'''

str=input('Enter string:')
print('This program will first take two integers a and b and snother two integers c and d then prints the caracters of the string from index a to b and from c to d')
a=int(input('enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
d=int(input('Enter d:'))
if a>b:
    a, b=b, a
if c>d:
    c, d=d, c
first_slice=str[a:b]
second_slice=str[c:d]
sliced_string=first_slice+second_slice
print(sliced_string)
