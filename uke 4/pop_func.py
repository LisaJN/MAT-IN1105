#4.1
import numpy as np
n = 48

def population(k,B,C,t):
    N = B/(1+C*np.exp(-k*t))
    return N

print('populasjon vekst:  Timer:')

for t in range(0,n+1,4): #lager en for-løkke for t-verdiene og printer ut tabellen
    print('%5.0f             %2.0f' %(population(0.2, 50000, 9, t),t))

"""
Terminal>pop_func.py
populasjon vekst:  Timer:
 5000              0
 9913              4
17749              8
27526             12
36580             16
42924             20
46552             24
48390             28
49263             32
49666             36
49849             40
49932             44
49970             48
"""

