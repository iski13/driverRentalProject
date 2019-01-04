import random, os, Driver, Place, Task, Assignment

TABU = []

def goal_function(assignments):
    result = 0
    for ass in assignments:
        result = result + (ass.nes_time / 60)*ass.driver.salary
    return result

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
    #                                   drivers[i][3], drivers[i][4], drivers[i][5], drivers[i][6]))   #Zamiennie dzialajace inicjalizacje
    listOfWorkers.append(Driver.Driver(drivers[i]))                                                    #lista lub pojedynczymi argumentami
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


for i in range(0, len(listOfTasks)-1):
    listOfTasks[i].show()                                   #Sortowanie zlecen wedlug godziny

#for i in range(0, len(listOfTasks)-1):
#    for j in range(i+1, len(listOfTasks)-1):
#        if listOfTasks[i].dest == listOfTasks[j].dest:
#            listOfTasks.append(listOfTasks[i] + listOfTasks[j])
#            listOfTasks.remove(listOfTasks[i])
#            listOfTasks.remove(listOfTasks[j])

for i in range(0, len(listOfTasks)-1):
    Task.Task.show(listOfTasks[i])


#----------------------------
#Komunikacja z uzytkownikiem:
#----------------------------

start = 0
stop = int(input("Podaj liczbe operacji (w minutach): "))
available = [] #Lista dostepnych w danej chwili
assigned = []

#Petla sterujaca
while start != stop:

#Zdejmowanie z listy TABU
    for i in TABU:
        TABU[i].susp_time = TABU[i].susp_time - 1
        if TABU[i].susp_time == 0:

            TABU.remove(TABU[i])



#Wybieranie jednej z mozliwosci



#Sprawdzanie mozliwosci

for j in listOfTasks:
    for i in listOfWorkers:
        if listOfWorkers[i].position == 0:
            available.append(listOfWorkers[i])
        else:
            continue
while len(available) > 0:
    num = random.randint(0,len(available))
    a = Assignment(available[num], listOfTasks[j],135)
    a.driver.available = False
    assigned.append(a)




#Wpisaywanie nowych elementow na liste TABU
    if goal_function(assigned) < goal_function(assigned_old):
        TABU.append(assigned_old)
        assigned_old = assigned
    else:
        TABU.append(assigned)



    start = start + 1

print(assigned)


