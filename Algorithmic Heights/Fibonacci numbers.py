'''
Algorithmic Heights
Fibonacci numbers

The Fibonacci numbers 0,1,1,2,3,5,8,13,21,34,… are generated by the following simple rule
Fn=Fn-1 + Fn-2 for n>1
Fn=1 for n=1
Fn=0 for n=0

Given: A positive integer n≤25.
Return: The value of Fn
'''

def fibonacci(num):
    #int-->int
    if num==0:
        return 0
    elif num==1:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)

n=int(input("enter an integer:"))
print("fibonacci of %d is %d" %(n,fibonacci(n)))