import numpy as np

lysår = 9.5*(10**15) #m
yr = 31556926 #sekunder
AU = 1.58*(10**(-5))*lysår
G = 6.674*(10**-11) #m^3 kg^−1 s^−1

Solmassen = ((4*np.pi**2)*(1*AU**3))/(G*(1*yr)**2)

print('Solmassen er %.3f kg' % Solmassen)

"""
Terminal> solarmass.py
Solmassen er 2008751565707058508644315299840.000 kg

Som er ≈ 2.01 · 10^30 kg.
"""
