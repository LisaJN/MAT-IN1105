#2.2
A = 1000  #initial amount in euros
p = 5     #interest rate in percent per year
n = 3     #years

money = A*(1+(p/100))**n

print('The amount 1000 euros has grown to in 3 years with a 5 percent interest rate is %.3f euros'% money)

"""
Terminal> Python interest_rate.py
The amount 1000 euros has grown to in 3 years with a 5 percent
interest rate is 1157.625 euros
"""
