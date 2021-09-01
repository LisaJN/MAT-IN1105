#2.7
a = 0
b = 5
n = 10

#a)
x = []
h = (b-a)/n
for i in range(n+1):
    x.append(a+i*h)
print(x)

"""
Terminal> python coor.py
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
"""
#b) bruke implisitt løkke
#x = [a+i*h for i in range(n+1)]
