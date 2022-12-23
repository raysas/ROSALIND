'''Python Village
2. Variables and Some Arithmetic'''

'''Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.'''

def pythagoras(a,b):
    '''returns the squre of the hypothesus of triangle of side lengths a and b'''
    hyp_sq=a**2+b**2
    return hyp_sq

def main():
    a=int(input('Enter first side of the right triangle:'))
    b=int(input('Enter second side of the right triangle:'))
    print("the square of the hypotenuse is:%d" % pythagoras(a,b))
