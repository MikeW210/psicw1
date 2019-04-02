import random
import matplotlib.pyplot as plot
import numpy as np
import math

x = list()
y = list()
city = list()
ammount = 10
tablica = ["Łódź","Warszawa","Zgierz","Katowice","Wrocław","Kraków", "Poznań", "Hel","Lublin", "Gdańsk"]





for i in range(ammount):
    x.append(random.randint(0, 40))
    y.append(random.randint(0, 40))
    city.append(i)

    print("City: " + tablica[i])
    print("Numer miasta: " + str(city[i]))
    print("Coordinate: " + "Y: " + str(y[i]) + "  X: " + str(x[i]))
   # colors = np.random.rand(ilosc)
    plot.scatter(x[i], y[i])
    if tablica[i] == "Łódź":
        start = 'Start + ' + tablica[i]
        plot.annotate(start, (x[i], y[i]))
    else:
        plot.annotate(tablica[i], (x[i], y[i]))


def shortestWay():
    tab = tablica
    city1 = city
    sh1 = list()
    sh2 = list()
    sh3 = list()
    now = 0
    print("*****************************************************************")
    for d in range(ammount-1):
        set1 = {}
        list1 = []
        list2 = []
        print("Jesteś w: " + tab[d])
        for ii in city1:
            if now != ii:
               cost = pow(pow(x[now] - x[ii], 2) + pow(y[now] - y[ii], 2), .5)
               set1.update({ii: cost})
               list1.append(cost)

               print("Droga do " + tab[ii] + " to: " + str(cost) + "km")
               list2.append(tab[ii])



        print("*****************************************************************")
        print(set1)
        print("*****************************************************************")

        now = min(set1, key=lambda k: set1[k])
        # points.pop(current)
        if len(set1) != 1:
            city1.remove(now)

        if 0 in city1:
            city1.remove(0)
        sh1.append(now)
        sh2.append(min(list1))
        sh3.append(list2)

    print('Takie są twoje odległości: ')
    print(sh2)
    print('Tak Wygląda twoja trasa: ')
    sh1.insert(0, 0)
    print(sh1)
    print('Tak Wyglądały twoje zestawy miast: ')
    print(sh3)
    return sh1


bestway = shortestWay()


for xx in bestway:

    if xx == bestway[-1]:
        plot.plot([x[xx], x[0]], [y[xx], y[0]])
    else:
        nextPoint = bestway[bestway.index(xx) + 1]
        plot.plot([x[xx], x[nextPoint]], [y[xx], y[nextPoint]])

plot.show()

