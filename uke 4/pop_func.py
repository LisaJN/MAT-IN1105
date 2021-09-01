#4.1
import numpy as np
n = 48

def population(k,B,C,t):
    N = B/(1+C*np.exp(-k*t))
    return N

for t in range(0,n+1,4): #lager en for-løkke for t-verdiene og printer ut tabellen
    print('Populasjon vekst: %5.0f Timer: %2.0f' %(population(0.2, 50000, 9, t),t))

"""
Terminal>pop_func.py
Populasjon vekst:  5000 Timer:  0
Populasjon vekst:  9913 Timer:  4
Populasjon vekst: 17749 Timer:  8
Populasjon vekst: 27526 Timer: 12
Populasjon vekst: 36580 Timer: 16
Populasjon vekst: 42924 Timer: 20
Populasjon vekst: 46552 Timer: 24
Populasjon vekst: 48390 Timer: 28
Populasjon vekst: 49263 Timer: 32
Populasjon vekst: 49666 Timer: 36
Populasjon vekst: 49849 Timer: 40
Populasjon vekst: 49932 Timer: 44
Populasjon vekst: 49970 Timer: 48
"""
