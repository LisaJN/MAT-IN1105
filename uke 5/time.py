#4.4

infile.open()

infile.readlines()
infile.readlines()
infile.readlines()

Fdegrees = []
Cdegrees = []

for line in infile:
    words = line.split()
    F = float(words[-1])
    C = (F-32)*5/9
    Fdegrees.append(F)
    Cdegrees.append(C)

infile.close()

print(Fdegrees)
print(Cdegrees)

outfile = open ('outfile.txt','w')

for F,C in zip(Fdegrees,Cdegrees):
    outfile.write(f'{F:7.2f} {C:7.2f}\n')
    #print(degrees,Cdegrees)

outfile.close()

#4.5
import sys

try:
    F = sys.argv[1]
    F = float(F)

except IndexError:
    Print('Missing argument in cmd line')
    exit()
except ValueError:
    print('Wrong format in cmd argument')
    exit()
#except:
#    print('unknown error')
#    exit()

C = (F-32)*5/9
print(f'{F:g} degrees Farenheit is {C:g} Celsius')

#4.13
import sys

v0 = float(sys.argv[1]) #3
t = float(sys.argv[2])  #0.6
g = 9.81
t_stop = 2*v0/g

if t < 0 or t > t_stop:
    raise ValueError(f't must be between 0 and {t_stop}')

y = v0*t - 0.5*g*(t**2)
print(y)

#
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3
n = 5
dx = 1/(n-1)

xlist = []
ylist = []
#xlist = np.zeros(n)
#ylist = np.zeros(n)

for i in range(n):
    x.append(i*dx)
    y.append(f(x[i]))

x = np.array(xlist)
y = np.array(ylist)
####

n = 5
x = np.linspace(0,1,n)
y = np.zeros(n)
for i in range(n):
    y[i] = f(x[i])

###
import numpy as np

def f(x):
    return x**3 + np.sin(x)*exp(-3*x)
x = 1.2
y = f(x)
#eventuelt
x = np.linspace(0,3,100001)
y = f(x)

####
w = np.linspace(0,3,31)

print(w[:]) #printer hele arrayen
print(w[:-2]:)
print(w[:-2]) #printer ut alle untatt de nest siste
print(w[::5]:)
print(w[::5]) #henter ut 5 element
print(w[2:-2:6]:)
print(w[2:-2:6]) #start stopp og steg,
#opp til men ikke inkludert de to siste, men 6 steglengde
