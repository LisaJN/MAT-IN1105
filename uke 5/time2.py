#5.9
import numpy as np
import matplotlib.pyplot as plt
"""
v0 = 10
g = 9.81

t_stop = 2*v0/g
t = np.linspace(0,t_stop,101)
y = v0*t - 0.5*g*t**2

plt.plot(t,y)
plt.title('Ball in vertical motion')
plt.xlabel('height [m]')
plt.ylabel('time [s]')
plt.legend(['y(t)'])
plt.savefig('time2.png')
plt.show()

#5.10
import sys
v0_list = sys.argv[1:]
g = 9.81

for v0 in v0_list:
    v0 = float(v0)
    t_stop = 2*v0/g
    t = np.linspace(0,t_stop,101)
    y = v0*t - 0.5*g*t**2
    plt.plot(t,y,label=f'v0={v0}')

plt.title('Ball in vertical motion')
plt.xlabel('height [m]')
plt.ylabel('time [s]')
plt.legend(v0_list)
#plt.savefig('time2_2.png')
plt.show()
#5.11
import sys
v0_list = sys.argv[1:]
g = 9.81

max_t = 0
max_y = 0

for v0 in v0_list:
    v0 = float(v0)
    t_stop = 2*v0/g
    if t_stop > max_t:
        max_t = t_stop

    t = np.linspace(0,t_stop,101)
    y = v0*t - 0.5*g*t**2
    if np.max(y)>max_y:
        max_y = np.max(y)

    plt.plot(t,y,'--',label=f'v0={v0}')

plt.title('Ball in vertical motion')
plt.xlabel('height [m]')
plt.ylabel('time [s]')
plt.grid()
plt.legend(v0_list)
plt.axis([0,max_t,0,max_y])
#plt.savefig('time2_3.png')
plt.show()
"""
#5.13
import sys

y0 = float(sys.argv[1])
theta = float(sys.argv[2])
v0 = float(sys.argv[3])

g = 9.81
a = -1.0/(2*v0**2)*g/(np.cos(theta)**2)
b = np.tan(theta)
c = y0

x1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)

x_max = max(x1,x2)
x = np.linspace(0,x_max,101)
y = a*x**2 + b*x + c

plt.plot(x,y)
plt.show()
