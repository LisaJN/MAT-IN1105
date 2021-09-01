#2.8
v0 = 1.5 #start hastighet
g = 9.81 #tyngde aks.
n = 20 # ønsket intervaller

a = 0 #nedre grense for t
b = (2*v0)/g # øvre grense for t
h = (b-a)/n # lenfde på hvert intervall

#a) løsning basert på for løkke
print('   t      y(t)')
#i blir definer i forløkken, eksisterer ikke på fohånd som variabel
for i in range(n+1):
    t = a + i*h
    y = v0*t - (0.5*g*t**2)
    print(f'{t:6.2f}  {y:6.2f}')

#b) løsning basert på while-løkke
print('')
print('   t      y(t)')
t = 0
eps = 1e-6
while t <= b + eps:
    y = v0*t - (0.5*g*t**2)
    print(f'{t:6.2f}  {y:6.2f}')
    t += h

"""
eduroam-193-157-161-133:desktop lisa$ python ball_table1.py
   t      y(t)
  0.00    0.00
  0.02    0.02
  0.03    0.04
  0.05    0.06
  0.06    0.07
  0.08    0.09
  0.09    0.10
  0.11    0.10
  0.12    0.11
  0.14    0.11
  0.15    0.11
  0.17    0.11
  0.18    0.11
  0.20    0.10
  0.21    0.10
  0.23    0.09
  0.24    0.07
  0.26    0.06
  0.28    0.04
  0.29    0.02
  0.31    0.00

   t      y(t)
  0.00    0.00
  0.02    0.02
  0.03    0.04
  0.05    0.06
  0.06    0.07
  0.08    0.09
  0.09    0.10
  0.11    0.10
  0.12    0.11
  0.14    0.11
  0.15    0.11
  0.17    0.11
  0.18    0.11
  0.20    0.10
  0.21    0.10
  0.23    0.09
  0.24    0.07
  0.26    0.06
  0.28    0.04
  0.29    0.02
  0.31    0.00
eduroam-193-157-161-133:desktop lisa$
"""
