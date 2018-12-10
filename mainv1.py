import random, os, Driver, Place, Task

TABU = []

#-----------------------------------------------
#Wczytanie z pliku do listy obiektow typu Driver

path1 = os.getcwd()
path1 = os.path.join(path1, 'drivers.txt')

listOfWorkers = []



file1 = open(path1,'r')
drivers = file1.read()
drivers = drivers.split("\n")
del drivers[len(drivers)-1]
for i in range(0,len(drivers)):
    drivers[i] = drivers[i].split("\t\t")
    # listOfWorkers.append(Driver.Driver(drivers[i][0], drivers[i][1], drivers[i][2],
    #                                   drivers[i][3], drivers[i][4], drivers[i][5], drivers[i][6]))   #Zamiennie działające inicjalizacje
    listOfWorkers.append(Driver.Driver(drivers[i]))                                                    #listą lub pojedynczymi argumentami
    listOfWorkers[i].show()

file1.close()


#-----------------------------------------------
#Wczytywanie z pliku do listy obiektow typu Task

listOfTasks = []
courses = []
s = []

path2 = os.getcwd()
path2 = os.path.join(path2, 'tasks.txt')
file2 = open(path2,'r')
courses = file2.read()
courses = courses.split("\n")
del courses[len(courses)-1]
for i in range(0,len(courses)):

    courses[i] = courses[i].replace(":", " ")
    courses[i] = courses[i].replace("\t\t"," ")
    courses[i] = courses[i].split(" ")
    # listOfTasks.append(Task.Task(courses[i][0], courses[i][1], courses[i][2], courses[i][3]))         #Inicjalizacja zadania osobnymi danymi
    listOfTasks.append(Task.Task(courses[i]))                                                           #Inicjalizacja z listy
file2.close()
listOfTasks.sort()


#for i in range(0, len(listOfTasks)-1):
#    listOfTasks[i].show()                                   #Sortowanie zleceń według godziny

for i in range(0, len(listOfTasks)-1):
        if listOfTasks[i].dest == listOfTasks[i+1].dest:
            listOfTasks.append(listOfTasks[i] + listOfTasks[i+1])
            listOfTasks.remove(listOfTasks[i])
            listOfTasks.remove(listOfTasks[i+1])

for i in range(0, len(listOfTasks)-1):
    Task.Task.show(listOfTasks[i])