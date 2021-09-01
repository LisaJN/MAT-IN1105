#3.4
s = 0
M = 3
k = 1

for i in range(M):
    s += 1/((2*k)**2)
    k += 1
print(s)
"""
Terminal>sum_for.py
0.3402777777777778
"""
"""
feil: definer k, sette inn () i formelen slik at den regner ut riktig,
legge til en k for hver runde gjennom loopen.
"""
