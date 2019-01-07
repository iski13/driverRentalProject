import math
import datetime

class Place:

    def __init__(self, spotnumber = "1"):                                               #Inicjalizacja nowej lokalizacji
        spotName = {"0": "Baza","1": "Baza", "2": "Lotnisko Balice", "3": "Lotnisko Pyzowice", "4": "Dworzec Glowny", "5": "Dworzec Plaszow"}
        spotCoordinates = {"0":[0, 0],"1": [0, 0], "2": [7, 3], "3": [-4, 0], "4": [6, -2], "5": [8, 2]}

        self.name = spotName[spotnumber]
        self.x = spotCoordinates[spotnumber][0]
        self.y = spotCoordinates[spotnumber][1]

    def dist(self, other):                                                              #Obliczanie odleglosci
        return math.sqrt(abs(self.x-other.x)**2+abs(self.y-other.y)**2)

    def show(self):                                                                     #Prezentacja lokalizacji
        print("Jestes w %s o wspolrzednych x = %d oraz y = %d" %(self.name, self.x, self.y))

    def show_dist(self, other):                                                         #Wyswietlenie odleglosci
        return print("Miedzy ",self.name," a ", other.name,"jest ", self.dist(other)," km.")

#----------
#Operatory:
#----------

    def __eq__(self, other):
        if self.dist(other)==0:
            return True
        else:
            return False
#------
#Testy:
#------

#a = Place(2)
#b = Place(5)
#a.show()
#b.show()
#a.show_dist(b)