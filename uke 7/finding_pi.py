#A.4
import numpy as np
x0 = 3.14  #gitt startverdi

def f(x):
    return np.sin(x)
    f = f(x)

#den deriverte av sin(x) = cos(x)
def d(x):
    return np.cos(x)
    d = d(x)

print('    Approximation     Exact')

def Newton(f,d,x):
    n = 0
    for n in range(1,3):                          #Skal bare ha x0, x1 og x2
        print(f'x{n-1}: {x:.13f}   {np.pi:.13f}') #Printer med 13 desimaler
        x = x - f(x)/d(x)                         #Newton metoden
        n += 1                                    #Legger til neste steg
    print(f'x{n-1}: {x:.13f}   {np.pi:.13f}')
Newton(f,d,x0)                                    #Kaller på funksjonen

"""
Terminal>finding_pi
    Approximation     Exact
x0: 3.1400000000000   3.1415926535898
x1: 3.1415926549364   3.1415926535898
x2: 3.1415926535898   3.1415926535898
"""
