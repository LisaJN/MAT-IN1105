#4.5
import numpy as np

def f(x):
    #setter opp funksjonen
    if np.sin(x) > 0:
        return np.sin(x)
    else:
        return 0

def test_f():
    """
    lager en testfunkjson for f(x)
    """
    expected, expected2 = 1,0
    computed,computed2 = f(np.pi/2),f(3*np.pi/2)
    tol = 1E-14
    success = abs(expected - computed) < tol
    success2 = abs(expected2 - computed2) < tol
    msg = f'computed={computed} != {expected}(expected)'
    msg2 = f'computed={computed2} != {expected2}(expected)'
    assert success, msg
    assert success2, msg2
test_f()

"""
Terminal>half_wave.py
"""
