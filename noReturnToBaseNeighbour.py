import os, Driver, Place, Task, Assignment, datetime
from generateDrivers import generateDrivers
from generateTasks import generateTasks
from startAssignment import startAssignment

#Generacja kierowców i zadań
generateDrivers()
generateTasks()

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
    listOfTasks.append(Task.Task(courses[i][0], courses[i][1], courses[i][2], courses[i][3]))         #Inicjalizacja zadania osobnymi danymi
    # listOfTasks.append(Task.Task(courses[i]))                                                           #Inicjalizacja z listy
    #print(listOfTasks[i])
file2.close()
listOfTasks.sort()
for i in range(0, len(listOfTasks)):
    listOfTasks[i].show()                                   #Sortowanie zleceń według godziny

#------------------------------------------------------
#ALGORYTM

round = 0
STOP = 500

places = []
for i in range(1,6):
    places.append(Place.Place(str(i)))

tabooList1 = []             #Lista zabronień kierowców
tabooDriver = []            #Pomocnicza^^^

tabooList2 = []             #Lista zabronień przypisań
tabooAssignments = []       #Pomocnicza^^^
period2 = 3                 #Okres zabronień przypisania

tabooList3 = []             #Lista zabronień kombinacji przypisań pamięć długotrwała

availableDriversTime = []   #Lista dostępnych kierowców według grafiku
availableDriversReal = []   #Lista dostępnych kierowców według zabronień


listOfAssignments = []      #Lista przypisań


period3 = 1
helpDriver = Driver.Driver()
data = []


#Wskaźniki jakości rozwiązania
numberOfHelp = 0
percentageK0 = 0.0
percentageK1 = 0.0
percentageK2 = 0.0
driversAfterHours = 0

startSolution = startAssignment(listOfWorkers,listOfTasks, helpDriver)

for assignment in startSolution:
    tabooList2.append([assignment, period2])
    tabooAssignments.append(assignment)
    listOfAssignments.append(assignment)

while round != STOP:
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
                driver[1] -= 1
                if driver[1] == 0:
                    tabooList1.remove(driver)
                    tabooDriver.remove(driver[0])
                    if (hour > driver[0].shift.hour + driver[0].work_time) or (hour == driver[0].shift.hour + driver[0].work_time and minute > driver[0].shift.minute):
                        driversAfterHours += 1

            for driver in listOfWorkers:
                if driver.shift.hour == hour and driver.shift.minute == minute :
                    availableDriversTime.append(driver)
                    availableDriversReal.append(driver)
                    # print("Zaczyna")

                # if (driver in tabooDriver) and (driver in availableDriversReal) :
                #     availableDriversReal.remove(driver)
                #     print("zabroniony")

                if not (driver in tabooDriver) and (driver in availableDriversTime) and not (driver in availableDriversReal) :
                    availableDriversReal.append(driver)
                    # print("Odzabroniony")

                if ((driver.shift.hour+driver.work_time == hour) and (driver.shift.minute == minute)) and (driver in availableDriversTime) :
                    availableDriversTime.remove(driver)
                    if driver in availableDriversReal :
                        availableDriversReal.remove(driver)
                    # print("zakonczyl")
            for task in listOfTasks:

                if task.start_time.hour == hour and task.start_time.minute == minute:
                        # task.show()
                        if availableDriversReal:
                            minDistance = 10**6
                            for driver in availableDriversReal:
                                if not ((Assignment.Assignment(driver, task)) in tabooAssignments) and task.dest.dist(driver.position)< minDistance:
                                    selected = driver
                                    minDistance = task.dest.dist(driver.position)
                                else:
                                    continue
                            if minDistance == 10**6:
                                selected = helpDriver
                        else:
                            selected = helpDriver

                        listOfAssignments.append(Assignment.Assignment(selected,task))

                        if selected == helpDriver:
                            numberOfHelp += 1
                        tabooList2.append([listOfAssignments[len(listOfAssignments) - 1], period2])  # Dodanie przypisanie do listy zabronień z okresem
                        tabooAssignments.append(listOfAssignments[len(listOfAssignments) - 1])

                        if task.tasktype == 1 and selected.id != "K!":
                            tabooList1.append([selected, int(listOfAssignments[len(listOfAssignments)-1].arrivalTime + 15)])
                            tabooDriver.append(selected)
                            # for driver in availableDriversReal:
                            #     driver.show()
                            availableDriversReal.remove(selected)
                            selected.position = task.dest   # Po podstawieniu pozostań na miejscu
                        elif task.tasktype == 0 and selected.id != "K!":
                            tabooList1.append([selected, int(listOfAssignments[len(listOfAssignments) - 1].nes_time)])
                            tabooDriver.append(selected)
                            # for driver in availableDriversReal:
                            #     driver.show()
                            availableDriversReal.remove(selected)
                            selected.position = places[0]  # Po odbiorze powrót do bazy


                        # listOfAssignments[len(listOfAssignments)-1].show()
    tabooList3.append(listOfAssignments)  # Dodanie kombinacji przyporządkowań do listy zabronień z okresem

    result = 3 * 8 * listOfWorkers[0].salary
    for assignment in listOfAssignments:
        if assignment.driver.fulltimer == 1:
            if assignment.driver.id == "K0":
                percentageK0 += assignment.nes_time / 60
            elif assignment.driver.id == "K1":
                percentageK1 += assignment.nes_time / 60
            elif assignment.driver.id == "K2":
                percentageK2 += assignment.nes_time / 60
        else:
            result = result + assignment.nes_time / 60 * assignment.driver.salary
        if assignment.driver.id == "K!":
            result = result + assignment.nes_time / 60 * assignment.driver.salary
        # else :
    percentageK0 = percentageK0 / 8 * 100
    percentageK1 = percentageK1 / 8 * 100
    percentageK2 = percentageK2 / 8 * 100
    goalFunction = result

    data.append([str(goalFunction), str(numberOfHelp), str(percentageK0), str(percentageK1), str(percentageK2),
                 str(driversAfterHours)])

    # Czyścimy!!!!
    availableDriversTime.clear()
    availableDriversReal.clear()
    listOfAssignments.clear()
    tabooList1.clear()
    tabooDriver.clear()
    percentageK0 = 0
    percentageK1 = 0
    percentageK2 = 0
    numberOfHelp = 0
    driversAfterHours = 0
    round += 1

# print(data)
data1 = []
for data in data:
    data1.append('\t'.join(data))
data = data1
print(data)
path = os.getcwd()                                          #Ustawienie ściezki do pliku na bieżący folder
path = os.path.join(path, 'results.csv')
resultStr = '\n'.join(data)
with open(path, 'w') as file:
    file.write(resultStr)