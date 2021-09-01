"""
##Les verdier fra bruker

x0 = float(input('Startbeløp? '))
p = float(input('Rente (%)? '))
N = int(input('Antall år? '))

## Beregn beløprt for hvert år

x = [0]*(N+1)
x[0] = x0

for n in range(1,N+1):
    x[n] = (1+p/100)*x[n-1]

##skriv ut tabell

print('')
print('År     Beløp')

for n in range (N+1):
    print(f'{n:3d}   {x[n]:7.2f}')

import sys
import matplotlib.pyplot as plt

#Les parametre fra kommandolinjen
x0 = int(sys.argv[1]) #startpop
M = int(sys.argv[2]) #bærekapasitet/makspop
a = float(sys.argv[3]) #vekstrate (0 = konstant pop)
N = 200

##Initier x
x = [0]*(N+1)
x[0] = x0

## beregn x[n] for n=1,2,3...., #N
for n in range(1,N+1):
    x[n] = x[n-1] + a*x[n-1] * (1-x[n-1]/M)

## Plott x[n] vs N
plt.plot(range(N+1),x)
plt.show()

##eks på kjøring:
## python time.py 50 200 0.3

def stern(N):
    x = [0]*(2*N) # x[0], x[1], ..., x[2N-1]
    x[0] = 0
    x[1] = 1
    for n in range(1,N):
        x[2*n] = x[n]
        x[2*n+1] = x[n] + x[n+1]
    #n = 1: x[2],x[3]
    #n = N-1: x[2*(N-1)] = x[2*N-2], x[2*(N-1)+1] = x[2*N-1]
    return x

def printrationals(N):
    x = stern(N)
    for n in range(2*N-1):
        print(f'{x[n]}/{x[n+1]}')
    #n=0:x[0]/x[1]
    #n=2*N-2:x[2*N-2]/x[2*N-1]
import sys
printrationals(int(sys.argv[1]))

#A.1 Langtangen
##a)
import numpy as np

def an(N):
    res = np.zeros(N+1)
    for n in range(N+1):
        res[n] = (7+1/(n+1))/(3-1/(n+1)**2)
    return res

a = an(100)
for n in range(len(a)):
    print(f'a_{n} = {a[n]:7.5f}')

import numpy as np
def Dn(N):
    res = np.zeros(N+1)
    for n in range(N+1):
        h = 2**(-n)
        res[n] = np.sin(h)/h
    return res

D = Dn(20)
for n in range(len(D)):
    print((f'D_{n} = {D[n]:7.5f}'))

import matplotlib.pyplot as plt
plt.plot(range(len(D)), D, 'ro')
plt.show()
"""
import numpy as np

def D(f,x,N):
    Dvec = np.zeros(N+1)
    for n in range(N+1):
        h = 2**(-n)
        Dvec[n] = (f(x+h))/h
    return Dvec

#Let f(x)=sin(x), x=0, N=80
f = np.sin
x = 0
N = 80
Dn = D(f,x,N)

import matplotlib.pyplot as plt

plt.plot(np.arange(0,N+1),Dn,'mo')
plt.show()
