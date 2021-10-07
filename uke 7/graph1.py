#6.14
import numpy as np
import matplotlib.pyplot as plt

#a)
#Setter opp funksjonen for punktene
def plot_line(p1, p2):
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    return x,y

#spesifiserer x og y koordinatene til å gå fra 1 til 4
#indekserer hvor de hører hjemme/start og slutt
plt.plot(plot_line((1,1),(1,4))[0],plot_line((1,1),(1,4))[1])
plt.plot(plot_line((1,1),(4,1))[0],plot_line((1,1),(4,1))[1])

plt.title('two lines')
plt.legend(['line 1','line 2'])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

#b)
#setter opp funksjonen på nytt og plotter uten plt.show
#markerer punktene
def plot_line(p1, p2):
    return plt.plot(p1,p2,'c-o',markerfacecolor='m')

#setter opp funksjonen med en for-løkke for å knytte alle punktene sammen
def complete_graph(points):
    for i in range(len(points)):
        for j in range(len(points)):
            plot_line((points[i][0],points[j][0]),\
            (points[i][1],points[j][1]))
#gitte verdier
corners = (0,0),(1,0),(0,1),(1,1)
alpha = (np.sqrt(2))/2
values = (1,0),(alpha,alpha),(0,1),(-alpha,alpha),\
(-1,0),(-alpha,-alpha),(0,-1),(alpha,-alpha)

complete_graph(corners)
plt.title('Square')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

complete_graph(values)
plt.title('Octagon')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
