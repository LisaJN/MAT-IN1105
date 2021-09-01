#2.3
primes = [2,3,5,7,11,13]

for e in primes:
    print(e)

"""
Terminal> Python primes.py
2
3
5
7
11
13
"""

p = 17

primes.append(p) #alternativ: primes = primes + [p]
for e in primes:
     print(e)

"""
Terminal> Python primes.py
2
3
5
7
11
13
17
"""
