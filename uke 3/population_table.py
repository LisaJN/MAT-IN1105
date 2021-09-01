#3.7
import numpy as np
B = 50000  #max size of population the enviroment can sustain indefinitely
k = 0.2    #population growth in h^-1
N = 5000   #initial value of pop.
t = 0      #initial value of time
n = 12     #number of elements in the list
C = (B/N-1)/(np.exp(-k*t)) #C value from population.py

N_list = [48/n*i for i in range(n+1)] #lager N_list

def population(t): #def. en funksjon som returnerer formelen fra population.py
    return B/(1+C*np.exp(-k*t))

t_list = [population(t) for t in N_list] #t_list

for N, t in zip(N_list, t_list): #zipper listene og printer dem
    print('Populasjon vekst: %5.0f Timer: %2.0f' %(N, t))

"""
Terminal>population_table.py
Populasjon vekst:     0 Timer: 5000
Populasjon vekst:     4 Timer: 9913
Populasjon vekst:     8 Timer: 17749
Populasjon vekst:    12 Timer: 27526
Populasjon vekst:    16 Timer: 36580
Populasjon vekst:    20 Timer: 42924
Populasjon vekst:    24 Timer: 46552
Populasjon vekst:    28 Timer: 48390
Populasjon vekst:    32 Timer: 49263
Populasjon vekst:    36 Timer: 49666
Populasjon vekst:    40 Timer: 49849
Populasjon vekst:    44 Timer: 49932
Populasjon vekst:    48 Timer: 49970
"""
