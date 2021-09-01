#5.1
import numpy as np

a = float(input("please enter value of a: "))
b = float(input("please enter value of b: "))
c = float(input("please enter value of c: "))

x_1 = (((-b)+(np.sqrt((b**2)-(4*a*c))))/(2*a))
x_2 = (((-b)-(np.sqrt((b**2)-(4*a*c))))/(2*a))

print(x_1,x_2)

"""
Terminal>quadratic_roots_input.py
please enter value of a: -6
please enter value of b: -1
please enter value of c: 2
<class 'float'>
-0.666666666667 0.5
"""
