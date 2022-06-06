'''Python Village
4. Conditions and Loops'''

'''Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.'''
print('This program will ask the user for 2 integers a and b and output the sum of all numbers in between a and b inclusively')
a=int(input('enter integer a:'))
b=int(input('enter integer b:'))
sum=0
if a>b:
    a, b=b, a
for i in range(a, b+1):
    if i%2!=0:
        sum+=i
print(sum)