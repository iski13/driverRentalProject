import os, Driver, Place, Task, Assignment, datetime
from generateDrivers import generateDrivers
from generateTasks import generateTasks

#Generacja kierowców i zadań
# generateDrivers()
# generateTasks()

#-----------------------------------------------
#Wczytanie z pliku do listy obiektow typu Driver

path1 = os.getcwd()
path1 = os.path.join(path1, 'drivers.txt')
listOfWorkers = []

file1 = open(path1,'r')
drivers = file1.read()
drivers = drivers.split("\n")
del drivers[len(drivers)-1]
#print(drivers)
for i in range(0,len(drivers)):
    drivers[i] = drivers[i].split("\t\t")
    print(drivers[i])
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
    #print(courses[i])
    # listOfTasks.append(Task.Task(courses[i][0], courses[i][1], courses[i][2], courses[i][3]))         #Inicjalizacja zadania osobnymi danymi
    listOfTasks.append(Task.Task(courses[i]))                                                           #Inicjalizacja z listy
    #print(listOfTasks[i])
file2.close()
listOfTasks.sort()
for i in range(0, len(listOfTasks)):
    listOfTasks[i].show()                                   #Sortowanie zleceń według godziny

#------------------------------------------------------
#ALGORYTM

round = 0
STOP = 100
tabooList1 = []             #Lista zabronień kierowców
tabooDriver = []            #Pomocnicza^^^

tabooList2 = []             #Lista zabronień przypisań
tabooAssignments = []       #Pomocnicza^^^

tabooList3 = []             #Lista zabronień kombinacji przypisań
tabooCombinations = []      #Pomocnicza^^^

availableDriversTime = []   #Lista dostępnych kierowców według grafiku
availableDriversReal = []   #Lista dostępnych kierowców według zabronień

listOfAssignments = []      #Lista przypisań

period2 = 1
period3 = 1
helpDriver = Driver.Driver()
data = []

while round != STOP :
    for assignment in tabooList2:
        if assignment[1] == 0:
            tabooList2.remove(assignment)
            tabooAssignments.remove(assignment[0])
            continue
        assignment[1] -= 1
        #assignment[0].show()

    for hour in range (8, 24):
        for minute in range (0,60):

            # print(hour,minute)

            for driver in tabooList1 :
                driver[1]-=1
                if driver[1] == 0 :
                    tabooList1.remove(driver)
                    tabooDriver.remove(driver[0])

            for driver in listOfWorkers:
                if driver.shiftH == hour and driver.shiftM == minute :
                    availableDriversTime.append(driver)
                    availableDriversReal.append(driver)
                    #print("Zaczyna")

                # if (driver in tabooDriver) and (driver in availableDriversReal) :
                #     availableDriversReal.remove(driver)
                #     print("zabroniony")

                if (driver in tabooDriver)==False and (driver in availableDriversTime) and (driver in availableDriversReal)==False :
                    availableDriversReal.append(driver)
                    # print("Odzabroniony")

                if ((driver.shiftH+driver.work_time == hour) and (driver.shiftM == minute)) and (driver in availableDriversTime) :
                    availableDriversTime.remove(driver)
                    if driver in availableDriversReal :
                        availableDriversReal.remove(driver)
                    #print("zakonczyl")



            for task in listOfTasks :
                minutes = int(task.dest.dist(Place.Place("1")) / Assignment.std_velocity * 60)    #Czas dojazdu od bazy

                if task.start_time.minute - minutes < 0 :                                       #Deklaracja rzeczywistej godziny rozpoczęcia
                    taskStart = datetime.time(task.start_time.hour-1, 59+task.start_time.minute - minutes)
                else:
                    taskStart = datetime.time(task.start_time.hour,task.start_time.minute-minutes)
                if taskStart.hour == hour and taskStart.minute == minute:
                    # task.show()
                    minDistance = 10**6


                    if availableDriversReal:
                        for driver in availableDriversReal:
                            # if tabooAssignments:
                                if not (Assignment.Assignment(driver, task) in tabooAssignments):
                                    minDistance = driver.position.dist(task.dest)
                                    selected = driver
                                    break
                                else:
                                    selected = helpDriver

                    else:
                        selected = helpDriver

                    listOfAssignments.append(Assignment.Assignment(selected,task))
                    tabooList2.append([listOfAssignments[len(listOfAssignments)-1],period2])    #Dodanie przypisanie do listy zabronień z okresem
                    tabooAssignments.append(listOfAssignments[len(listOfAssignments) - 1])

                    # if task.tasktype == 1 :
                    #     tabooList1.append([selected, int(listOfAssignments[len(listOfAssignments)-1].arrivalTime) + 15])
                    #     tabooDriver.append(selected)
                    #     availableDriversReal.remove(selected)
                    #     selected.position = task.dest
                    # else:
                    if selected.id != "K!":
                        tabooList1.append([selected, int(listOfAssignments[len(listOfAssignments)-1].nes_time)])
                        tabooDriver.append(selected)
                        #selected.show()
                        availableDriversReal.remove(selected)
                        selected.position = Place.Place(str(1))     #Po każdym zleceniu powrót do bazy!!! (uproszczenie)
                    # else:


                    # listOfAssignments[len(listOfAssignments)-1].show()


    tabooList3.append([listOfAssignments, period3])        #Dodanie kombinacji przyporządkowań do listy zabronień z okresem

    result = 3*8*listOfWorkers[0].salary
    for assignment in listOfAssignments :
        if assignment.driver.fulltimer == 0 :
            result = result + assignment.nes_time/60 * assignment.driver.salary
        if assignment.driver.id=="K!" :
            result = result + assignment.nes_time/60 *assignment.driver.salary
        # else :

    data.append(str(result))

    availableDriversTime.clear()
    availableDriversReal.clear()
    listOfAssignments.clear()
    tabooList1.clear()
    tabooDriver.clear()

    round += 1
print(data)
path = os.getcwd()                                          #Ustawienie ściezki do pliku na bieżący folder
path = os.path.join(path, 'results.csv')
resultStr = '\n'.join(data)
with open(path, 'w') as file:
    file.write(resultStr)