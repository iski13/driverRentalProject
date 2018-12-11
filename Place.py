import math, ProjectHeader

SpotName = {0: "Baza", 1: "Spot1", 2: "Spot2", 3: "Spot3", 4: "Spot4", 5:"Spot5"}
SpotCoordinates = {0: [0, 0], 1: [7, 3], 2: [-4, 0], 3: [6, -2], 4: [8, 2], 5: [-1, -5]}

class Place:

    def __init__(self, spotnumber = 0):                                               #Inicjalizacja nowej lokalizacji

        self.name = SpotName[spotnumber]
        self.x = SpotCoordinates[spotnumber][0]
        self.y = SpotCoordinates[spotnumber][1]

    def dist(self, other):                                                              #Obliczanie odleglosci
        return math.sqrt(abs(self.x-other.x)**2+abs(self.y-other.y)**2)

    def show(self):                                                                     #Prezentacja lokalizacji
        print("Jesteś w %s o współrzędnych x = %d oraz y = %d" %(self.name, self.x, self.y))

    def show_dist(self, other):                                                         #Wyswietlenie odleglosci
        return print("Między ",self.name," a ", other.name,"jest ", self.dist(other)," km.")

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