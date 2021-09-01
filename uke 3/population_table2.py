#3.8
import numpy as np
B = 50000  #max size of population the enviroment can sustain indefinitely
k = 0.2    #population growth in h^-1
N = 5000   #initial  condition
t = 48     #slutt tid
n = 12     #antall verdier vi ønsker
C = 9      #c verdi fra population.py
dt = t/n   #tidsinterval
t1 = []    #tom liste
N1 = []    #tom liste

for i in range(n+1):
    tid = i * dt
    population = B/(1+C*np.exp(-k*tid))
    t1.append(tid)
    N1.append(population)

print("Tid: Populasjon:")
tN1 = [t1, N1]         #ny liste med verdiene fra t1 og N1
for t1, N1 in zip(tN1[0], tN1[1]):
    print("%2.f %5.f" %(t1, N1))  #zipper listene og printer

print('------------') #printer en strek slik at det ser litt ryddig ut

tN2 = [] #tom liste
for t1,N1 in zip(tN1[0], tN1[1]): #zipper de to listene inn i tN2 og printer
    tN2.append([t1, N1])

print("Tid: Populasjon:")
for i in range(len(tN2)):
    print("%2.f %5.f" %(tN2[i][0], tN2[i][1]))

"""
Terminal>population_table2.py
Tid: Populasjon:
 0  5000
 4  9913
 8 17749
12 27526
16 36580
20 42924
24 46552
28 48390
32 49263
36 49666
40 49849
44 49932
48 49970
------------
Tid: Populasjon:
 0  5000
 4  9913
 8 17749
12 27526
16 36580
20 42924
24 46552
28 48390
32 49263
36 49666
40 49849
44 49932
48 49970
"""
