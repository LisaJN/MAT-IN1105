#Exercise 2.4: Generate odd numbers

n = 20
a = 1
while a <= n:
    print(a)
    a += 2   #a = a+2

#alternativ: kjip versjon
a = 1
while a <= n:
    if a%2 == 1:
        print(a)
    a += 1

"""
Terminal> python odd.py
1
3
5
7
9
11
13
15
17
19
"""
