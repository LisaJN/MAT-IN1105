#3.4
s = 0
M = 3
k = 1

for k in range(1,M+1):
    s += 1/((2*k)**2)
print(s)

"""
Terminal> sum_for.py
0.3402777777777778
"""
"""
feil: definer k, sette inn () i formelen slik at den regner ut riktig, sette
range fra 1 til M+1
"""
