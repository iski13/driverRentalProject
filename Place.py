import math
import datetime

class Place:

    def __init__(self, spotnumber = "1"):  #Inicjalizacja nowej lokalizacji

        spotName = {"1": "Baza", "2": "Spot1", "3": "Spot2", "4": "Spot3", "5": "Spot4"}
        spotCoordinates = {"1": [0, 0], "2": [7, 3], "3": [-4, 0], "4": [6, -2], "5": [8, 2]}

        self.name = spotName[spotnumber]
        self.x = spotCoordinates[spotnumber][0]
        self.y = spotCoordinates[spotnumber][1]
        self.spotNumber = spotnumber

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def dist(self, other):                                                     #Obliczanie odleglosci
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

    def show(self):                                                                 #Prezentacja lokalizacji
        print("Jesteś w %s o współrzędnych x = %d oraz y = %d" %(self.name, self.x, self.y))

    def show_dist(self, other):                                                 #Wyswietlenie odleglosci
        return print("Między ",self.name," a ", other.name,"jest ", self.dist(other)," km.")

#Testy:

