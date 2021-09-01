#5.10
import numpy as np

def extract_data(filename):
    infile = open(filename, 'r')
    infile.readline()[1:]
    T = []
    for line in infile:
        words = line.split()
        for i in words:
            temp = float(i)
            T.append(temp)
    infile.close()
    return T
#kaller på funksjonen og ber den hente informasjon fra txt filene
oct_1945 = extract_data('temp_oct_1945.txt')
oct_2014 = extract_data('temp_oct_2014.txt')

#gjør utregningene direte i printfunksjonen
print(f'mean value of temp in 1945: {np.mean(oct_1945):.2f}   mean value of temp in 2014: {np.mean(oct_2014):.2f} \n\
max value of temp in 1945: {np.max(oct_1945)}    max value of temp in 2014: {np.max(oct_2014)} \n\
min value of temp in 1945: {np.min(oct_1945)}     min value of temp in 2014: {np.min(oct_2014)}')

def write_formatting(filename,list1,list2):
    outfile = open(filename, 'w')
    for a,b in zip(list1,list2):
        outfile.write(f'{a}    {b}\n')
    outfile.close()

#kaller på funksjonen og ber den lage en ny fil med gitt informasjon
write_formatting('temp_formatted.txt', oct_1945, oct_2014)

"""
Terminal>temp_read_write.py
mean value of temp in 1945: 6.51   mean value of temp in 2014: 8.85
max value of temp in 1945: 11.6    max value of temp in 2014: 13.6
min value of temp in 1945: 2.1     min value of temp in 2014: 2.3
"""
