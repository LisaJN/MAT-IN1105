#A.2
def x(n):
    if n==0 or n==1:       #Setter de to første elementene lik 1
        return 1
    return x(n-1) + x(n-2) #Setter opp diff likningen
for n in range(0,15):      #Velger de 15 første elementene
    print('x%g = %g' %(n,x(n)))

"""
Terminal>fibonacci.py
x0 = 1
x1 = 1
x2 = 2
x3 = 3
x4 = 5
x5 = 8
x6 = 13
x7 = 21
x8 = 34
x9 = 55
x10 = 89
x11 = 144
x12 = 233
x13 = 377
x14 = 610
"""
