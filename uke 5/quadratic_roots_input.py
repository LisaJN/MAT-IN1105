#5.1
import numpy as np

a = float(input('please enter value of a: '))
b = float(input('please enter value of b: '))
c = float(input('please enter value of c: '))

x_1 = (((-b)+(np.sqrt((b**2)-(4*a*c))))/(2*a))
x_2 = (((-b)-(np.sqrt((b**2)-(4*a*c))))/(2*a))

print(f'{x_1:.2f}',f'{x_2:.2f}')

"""
Terminal>quadratic_roots_input.py
please enter value of a: -6
please enter value of b: -1
please enter value of c: 2
-0.67 0.50
"""
