#2.15
q = [['a','b','c'],['d','e','f'],['g','h']]
#a)


#q av -1 er det siste elementet i lista, altså [g,h], -2 refererer til nest siste element
#i den lista altså g.
#b)
for i in q:
    for j in range(len(i)):
        print(i[j])
#i vil være lister, mens j løper gjennom en range så det er et heltall.
