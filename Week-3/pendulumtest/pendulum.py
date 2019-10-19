L=int(raw_input('Enter the length of the pendulum: '))
g=float(raw_input('Enter the accn due to gravity: '))


def period(L,g):
    isinstance(L,int)
    print (isinstance (L, int))
    if isinstance (L, int)==False:
        print ('you have a Type error. Make sure the number you inputed is an integer')
    isinstance(g,int)
    print (isinstance (g, float))
    if isinstance (g, float)==False:
        print ('you have a Type error. Make sure the number you inputed is a float')
    
    
    if isinstance (L, int)== True and isinstance (g, float)==True:
        import math
        W= math.sqrt(L/g)
        T=2*math.pi*W
        return T
    else:
        print ('The sum could not be computed due to type errors')



print (period(L,g))

