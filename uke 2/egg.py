import numpy as np

#The following formula expresses the time t it takes (in seconds)
#for the center of the yolk to reach the temperature Ty (in Celsius degrees):

T_w = 100      #temp boiling water
T_y = 70       #temp of yolk
T_0 = 20       #4, initial temp

M = 67         #47g small egg, 67g for large egg
p = 1.038      #gcm^-3, density
c = 3.7        #Jg^-1K^-1, specific heat capacity
K = 5.4*10**-3 #Wcm^-1K^-1, thermal conductivity

t = (((M**(2/3))*c*(p**(1/3)))/(K*((np.pi)**2)*(4*(np.pi)/3)**(2/3)))*(np.log(0.76*((T_0 - T_w)/(T_y - T_w))))

print('tiden det tar for eggeplommen å nå 70C er %.3f sekunder' % t)

"""
for T_0 = 4
Terminal> Python egg.py
tiden det tar for eggeplommen å nå 70C er 396.576 sekunder

Som tilsvarer rundt 7 minutter.

for T_0 = 20
Terminal> Python egg.py
tiden det tar for eggeplommen å nå 70C er 315.218 sekunder

Som tilsvarer 5 1/2 minutter.
"""
