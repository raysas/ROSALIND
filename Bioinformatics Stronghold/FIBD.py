#!/usr/bin/env python

'''Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

fibonacci formula if fn=fn-1 + fn-2;
starting month m (fm), fm=fm-1 + fm-2 - f0
hence for n>m: fn = fn-1 + fn-2 - fn-m
'''
def mortalFib(n,m):
    '''takes the month number n and the month span m and returns the number of living rabbits after n months'''
    dp=[0,1,1];a=0;new=0
    for i in range(3,n+1):
        if i<m+1:
            a=dp[i-1]+dp[i-2]
            new=a-dp[i-1]
            # print(new)
        elif i==m+1:
            a=dp[i-1]+dp[i-2]-1
        else:
            # print(new)
            a=dp[i-1]+dp[i-2] - dp[i-m-1]
        dp.append(a)
    print(dp)
    return dp[n]

a=int(input('enter month:'))
b=int(input('enter life span in months:'))
print(mortalFib(a,b))
