#3.11
M_C = 12.011 #g/mol
M_H = 1.0079 #g/mol
n = 2 #amount of carbon atoms
m = 2*n + 2 #Hydrogen in relation to Carbon

def m_m(n,m): #func for molar mass
    return n*M_C + m*M_H

print(f'M(C{n}H{m}) = {m_m(n,m):.3f} g/mol')

"""
Terminal>alkane.py
M(C2H6) = 30.069 g/mol
"""
