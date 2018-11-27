import math
import datetime

class Place:
    def __init__(self, name = 'Lotnisko',x = 0, y = 0, car_time = time(1,0), bus_time = time(1,30)):  #Inicjalizacja nowej lokalizacji
        self.name = name
        self.x = x
        self.y = y
        self.car_time = car_time
        self.bus_time = bus_time

    def dist(self, p1 = Place):                                                     #Obliczanie odleglosci
        return math.sqrt(abs(self.x-p1.x)**2+abs(self.y-p1.y)**2)

    def show(self):                                                                 #Prezentacja lokalizacji
        print("Do",self.name,"jest:")
        print("Samochodem:\t",self.car_time)
        print("Autobusem:\t",self.bus_time)
        if self.car_time < self.bus_time:
            return print("Szybciej będzie samochodem")
        elif self.car_time > self.bus_time:
            return print("Jedz autobusem")
        else:
            return print("Twoj wybor!")

    def show_dist(self, p = Place):                                                 #Wyswietlenie odleglosci
        return print("Między ",self.name," a ", p.name,"jest ", self.dist(p)," km.")

#Testy:

#p = Place('Lotnisko',20,20)
#q = Place('Dworzec',30,30)
#print(p.dist(q))
#p.show()
#p.show_dist(q)
#p.bus_time = time(0,25)
#p.show()
#p.show_dist(q)
