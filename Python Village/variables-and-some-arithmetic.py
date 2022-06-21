'''Python Village
2. Variables and Some Arithmetic'''

'''Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.'''

a=int(input('Enter first side of the right triangle:'))
b=int(input('Enter second side of the right triangle:'))
hyp_sq=a**2+b**2
print("the square of the hypotenuse is",end=':')
print(hyp_sq)
