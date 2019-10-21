import math

L=float(raw_input('Enter the length of the pendulum: '))
g=float(raw_input('Enter the accn due to gravity: ')

def period(L,g):
    
    isinstance(L,float)
    if isinstance (L, float)==False:
        print ('you have a Type error. Make sure the number you inputed is a floating point number')
    isinstance(g,float)
    if isinstance (g, float)==False:
        print ('you have a Type error. Make sure the number you inputed is a floating point number')
    if isinstance (L, float)==True and isinstance (g, float)==True:
        W= math.sqrt(L/g)
        T=2*math.pi*W
        return T
    else:
       print ('The sum could not be computed due to type errors')

print (period(L,g))


