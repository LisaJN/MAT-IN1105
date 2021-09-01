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
    msg = f"computed={computed} != {expected}(expected)"
    msg = f"computed={computed2} != {expected2}(expected)"
    assert success, msg
test_f()
