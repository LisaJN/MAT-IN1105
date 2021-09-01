#A.2
def x(n):
    if n==0 or n==1:
        return 1
    return x(n-1) + x(n-2)
for n in range(0,15):
    print('x_%g = %g' %(n, x(n)))

"""
Terminal>fibonacci.py
x_0 = 1
x_1 = 1
x_2 = 2
x_3 = 3
x_4 = 5
x_5 = 8
x_6 = 13
x_7 = 21
x_8 = 34
x_9 = 55
x_10 = 89
x_11 = 144
x_12 = 233
x_13 = 377
x_14 = 610
"""
