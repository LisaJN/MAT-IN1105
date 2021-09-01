#5.4
import numpy as np

a = float(input("please enter value of a: "))
b = float(input("please enter value of b: "))
c = float(input("please enter value of c: "))

if (b**2-4*a*c)<0:
    print('Error: complex roots')
else:
    x_1 = (((-b)+(np.sqrt((b**2)-(4*a*c))))/(2*a))
    x_2 = (((-b)-(np.sqrt((b**2)-(4*a*c))))/(2*a))
    print(x_1,x_2)
"""
Terminal>quadratic_roots_error2.py
please enter value of a: 1
please enter value of b: 1
please enter value of c: 1
Error: complex roots

Terminal>quadratic_roots_error2.py
please enter value of a: -1
please enter value of b: 0
please enter value of c: 1
-1.0 1.0
"""
