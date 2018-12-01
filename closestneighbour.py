import os,math,
class Place:
    def __init__(self, wspX=0, wspY=0):
        self.wspX = wspX
        self.wspY = wspY

    def show(self):
        print("Współrzędne zlecenia to %d oraz %d" %(self.wspX, self.wspY))
    def dist(self, p1):                                                     #Obliczanie odleglosci
        return math.sqrt(abs(self.x-p1.x)**2+abs(self.y-p1.y)**2)






class Task():

    def __init__(self, start_time = datetime.time(18,0), tasktype = 1, dest = Place()):            #Inicjalizacja zadania
        self.start_time = start_time
        self.tasktype = tasktype
        self.dest = dest

    def show(self):                                                                 #Prezentacja zadania
        if self.tasktype==1:
            return print("Dostarczenie na\t",self.start_time,"\tz\t",self.dest.name)
        else:
            return print("Odebranie o\t\t",self.start_time,"\tz\t",self.dest.name)



availablePoints = {'1': [0, 0], '2': [7,3], '3': [-4, 0], '4': [6, -2], '5': [8, 2]}
iteration = 0
STOP = int(input("Podaj liczbę iteracji: "))
# czasRealizacjiZlecenia???





#-----------------------------------------------
#Wczytanie z pliku do listy obiektow typu Driver


path = os.getcwd()
path = os.path.join(path, 'drivers.txt')
workers = []

file = open(path,'r')
drivers = file.read()
drivers = drivers.split("\n")
del drivers[len(drivers)-1]
#print(drivers)
for i in range(0,len(drivers)):
    drivers[i] = drivers[i].split("\t\t")






#-----------------------------------------------
#Wczytywanie z pliku do listy obiektow typu Task

tasks = []
courses = []
s = []

path2 = os.getcwd()
path2 = os.path.join(path2, 'tasks.txt')
file = open(path2,'r')
courses = file.read()
courses = courses.split("\n")
del courses[len(courses)-1]
for i in range(0,len(courses)):
    courses[i] = courses[i].replace(":"," ")
    s.append(''.join(courses[i]))
    s[i] = s[i].replace("\t\t"," ")
    s[i] = s[i].split(' ')


print(s)

points = []

x0=[]

for place in s:
    points.append(Place(availablePoints[place[3]][0], availablePoints[place[3]][1]))
i=0
for eses in s:
    if i==len(drivers):
        i=0
    x0.append(drivers[i][0])
    i+=1
print(x0)                               #Rozwiązanie startowe


while iteration!=STOP:

