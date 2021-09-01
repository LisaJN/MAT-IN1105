#Exercise 2.1: Make a Fahrenheit-Celsius conversion table
#F = []
#C = F - 32*(5/9)
F = 0
steps = 10

while F <= 100:
    C = F-(32*(5/9))
    #print with 6 digits in total, 2 decimals:
    print('Fahrenheit %.2f Celsius %.2f' %(F,C))
    F = F + steps
"""
Terminal> Python f2c_table_while.py
Fahrenheit 0.00 Celsius -17.78
Fahrenheit 10.00 Celsius -7.78
Fahrenheit 20.00 Celsius 2.22
Fahrenheit 30.00 Celsius 12.22
Fahrenheit 40.00 Celsius 22.22
Fahrenheit 50.00 Celsius 32.22
Fahrenheit 60.00 Celsius 42.22
Fahrenheit 70.00 Celsius 52.22
Fahrenheit 80.00 Celsius 62.22
Fahrenheit 90.00 Celsius 72.22
Fahrenheit 100.00 Celsius 82.22
"""
