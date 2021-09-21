#5.4
import numpy as np

a = float(input('please enter value of a: '))
b = float(input('please enter value of b: '))
c = float(input('please enter value of c: '))

temp = b**2 - 4*a*c

if temp < 0:
    raise ValueError('Values for a, b, and c yield complex roots')

else:
    x_1 = (((-b)+(np.sqrt((b**2)-(4*a*c))))/(2*a))
    x_2 = (((-b)-(np.sqrt((b**2)-(4*a*c))))/(2*a))
    print(f'{x_1:.2f}',f'{x_2:.2f}')

"""
Terminal>quadratic_roots_error2.py
please enter value of a: 1
please enter value of b: 1
please enter value of c: 1
Traceback (most recent call last):
  File "quadratic_roots_error2.py", line 11, in <module>
    raise ValueError('Values for a, b, and c yield complex roots')
ValueError: Values for a, b, and c yield complex roots

Terminal>quadratic_roots_error2.py
please enter value of a: -1
please enter value of b: 0
please enter value of c: 1
-1.00 1.00
"""
