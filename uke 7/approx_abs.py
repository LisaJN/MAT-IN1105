#6.13
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi,np.pi, 1e-4)

def abs_approx(x):
    sum_ = 0
    for i in range(1, 5):
        sum_ += np.cos((2*i - 1)*x)/(((2*i)-1)**2)
    sum_ *= (4/np.pi)
    return (np.pi/2) - sum_

plt.plot(x,np.abs(x), label = 'Exact')
plt.plot(x,abs_approx(x), '--', label = 'Approximarion')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
