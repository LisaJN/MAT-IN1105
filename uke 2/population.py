#2.3
import numpy as np
B = 50000 #max size of population the enviroment can sustain indefinitely
k = 0.2 #population growth in h^-1
N_0 = 5000 #initial  condition

#snur på formelen for å finne uttrykk for C når t = 0
#N_0=B/(1+C*(np.exp**k*0)) -> N_0=B/1+C*1 -> C*N_0+N_0=B -> C=(B-N_0)/N_0

C = (B-N_0)/N_0
print(C)
"""
Terminal> python population.py
9.0
"""
N_24 = B/(1+C*np.exp(-k*24))

print('After 24 hours the poulation is at %.2f'% N_24)

"""
Terminal> Python population.py
After 24 hours the poulation is at 46552.00
"""
