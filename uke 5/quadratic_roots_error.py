#5.3
import numpy as np
import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

except IndexError:
    print('too few arguemnts')
    a = float(input('please enter value of a: '))
    b = float(input('please enter value of b: '))
    c = float(input('please enter value of c: '))

x_1 = (((-b)+(np.sqrt((b**2)-(4*a*c))))/(2*a))
x_2 = (((-b)-(np.sqrt((b**2)-(4*a*c))))/(2*a))
print(f'{x_1:.2f}',f'{x_2:.2f}')

"""
Terminal>quadratic_roots_error.py -1 0 1
-1.00 1.00

Terminal>quadratic_roots_error.py
too few arguemnts
please enter value of a: -6
please enter value of b: -1
please enter value of c: 2
-0.67 0.50
"""
