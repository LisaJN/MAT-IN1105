#3.7
import numpy as np
B = 50000  #max size of population the enviroment can sustain indefinitely
k = 0.2    #population growth in h^-1
N = 5000   #initial value of pop.
t = 0      #initial value of time
n = 12     #number of elements in the list
C = (B/N-1)/(np.exp(-k*t)) #C value from population.py

t_list = [48/n*i for i in range(n+1)] #lager t_list

def population(t): #def. en funksjon som returnerer formelen fra population.py
    return B/(1+C*np.exp(-k*t))

N_list = [population(t) for t in t_list] #N_list

print('Populasjon vekst:    Timer:')

for N, t in zip(N_list, t_list): #zipper listene og printer dem
    print('%2.f'%N,'               ','%.f'%t)

"""
Terminal>population_table.py
Populasjon vekst:    Timer:
5000                 0
9913                 4
17749                 8
27526                 12
36580                 16
42924                 20
46552                 24
48390                 28
49263                 32
49666                 36
49849                 40
49932                 44
49970                 48
"""
