#5.7
infile = open("Oxygen.txt")
mass = 0

lines = infile.readlines()[2:] #ber python lese fra og med linje 2 i Oxygen.txt

for line in lines:
    words = line.split()  #bruker line split for å dele opp
    mass += float(words[1])*float(words[2]) #henter ut 1 (weight) og 2 (natural_abundance) som lister
    #og regner ut g/mol for alle elementene til sammen i listene 
infile.close()

print(f'The molar mass of oxygen is {mass:g} g/mol')

"""
Terminal>read_file_isotopes.py
The molar mass of oxygen is 15.9994 g/mol
"""
