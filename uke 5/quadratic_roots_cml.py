#5.2
import sys
import numpy as np

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

x_1 = (((-b)+(np.sqrt((b**2)-(4*a*c))))/(2*a))
x_2 = (((-b)-(np.sqrt((b**2)-(4*a*c))))/(2*a))
print(x_1,x_2)

"""
Terminal>quadratic_roots_cml.py -1 1 0
-0.0 1.0
"""
