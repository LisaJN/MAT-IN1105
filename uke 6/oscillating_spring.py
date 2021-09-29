#6.4
import numpy as np
import matplotlib.pyplot as plt

A = 0.3      #lengden målt i m
k = 4.0      #[kg/(s**2)]
y = 0.0      #start høyden målt i m
m = 9.0      #massen av steinen målt i kg
gamma = 0.15 #[s**(-1)]
n = 101
dt = 0.24

def y(t):
    return A*np.exp((-gamma)*t)*np.cos(np.sqrt(k/m)*t)

t_array = np.zeros(n) #tom array
y_array = np.zeros(n) #tom array

for i in range(n):    #lager en for-løkke som fyller arrayene med y og t verdier
    t_array[i] = i*dt
    y_array[i] = y(t_array[i])

t_array_2 = np.linspace(0,24,101) #lager en ny t_array med linspace
y_array_2 = y(t_array_2)          #lager en ny y_array og kaller på y(t) med nye t_array

plt.plot(t_array,y_array, 'mo')
plt.plot(t_array_2,y_array_2, 'c')
plt.title('Oscillating Spring')
plt.xlabel('tid [s]')
plt.ylabel('posisjon [m]')
plt.legend(['y(t_array)','y(t_array_2)'])
plt.show()

"""
Terminal>oscillating_spring.py
"""
#se vedlegg: oscillating_spring.png
