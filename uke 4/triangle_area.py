#4.4
import numpy as np

h1,h2,h3 = [0,0],[1,0],[0,2]

def triangle_area(vertices):
    """
    setter opp x og y slik at de kaller på riktig element i vertices, og i h1, h2 og h3.
    """
    x1,x2,x3 = vertices[0][0],vertices[1][0],vertices[2][0]
    y1,y2,y3 = vertices[0][1],vertices[1][1],vertices[2][1]
    A = (1/2)*np.abs((x2*y3) - (x3*y2) - (x1*y3) + (x3*y1) + (x1*y2) - (x2*y1))
    return A

def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1, v2, v3 = [0,0],[1,0],[0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f'computed area={computed} != {expected}(expected)'
    assert success, msg
test_triangle_area()

"""
Terminal>triangle_area.py 
"""
