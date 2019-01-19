import os, Driver, Place, Task, Assignment, datetime
from generateDrivers import generateDrivers
from generateTasks import generateTasks
from startAssignment import startAssignment
from sortFunctions import sortShort, sortLong

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
fullDriver = []
partDriver = []

for driver in listOfWorkers:
    if driver.fulltimer == 1:
        fullDriver.append(driver)
    else:
        partDriver.append(driver)



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

listOfTasks = sortShort(listOfTasks)

for i in range(0, len(listOfTasks)):
    listOfTasks[i].show()                                   #Sortowanie zleceń według godziny

#------------------------------------------------------
#ALGORYTM


round = 0
STOP = 1
tabooList1 = []            #Lista zabronień kierowców
tabooDriver = []            #Pomocnicza^^^

tabooList2 = []             #Lista zabronień przypisań
tabooAssignments = []       #Pomocnicza^^^
period2 = 1                 #Okres zabronień przypisania

tabooList3 = []             #Lista zabronień kombinacji przypisań pamięć długotrwała

availableDriversTime = []   #Lista dostępnych kierowców według grafiku
availableDriversReal = []   #Lista dostępnych kierowców według zabronień
unavailableToTask =[]

listOfAssignments = []      #Lista przypisań


period3 = 1
helpDriver = Driver.Driver()
data = []
combinations = []
lista = []

#Wskaźniki jakości rozwiązania
numberOfHelp = 0
percentageK0 = 0.0
percentageK1 = 0.0
percentageK2 = 0.0
driversAfterHours = 0

startSolution = startAssignment(listOfWorkers, listOfTasks, helpDriver)

# for assignment in startSolution:
#     tabooList2.append([assignment, period2])
#     tabooAssignments.append(assignment)
#     listOfAssignments.append(assignment)

while round != STOP:
    for assignment in tabooList2:
        if assignment[1] == 0:
            tabooList2.remove(assignment)
            tabooAssignments.remove(assignment[0])
            continue
        assignment[1] -= 1
        #assignment[0].show()

    for task in listOfTasks:
        ifAssigned = 0
        for element in tabooList1:
            if element[1] <= task.start_time and element[2] >= task.start_time:
                unavailableToTask.append(element[0])
        for driver in listOfWorkers:
            if tabooList1:
                if driver in unavailableToTask:
                    continue
                else:
                    if task.start_time >= driver.shift and task.start_time <= driver.endTime :
                        selected = driver
                        if Assignment.Assignment(selected, task) in tabooAssignments:
                            continue
                        tabooList2.append([Assignment.Assignment(selected, task), period2])
                        tabooAssignments.append(Assignment.Assignment(selected, task))
                        listOfAssignments.append(Assignment.Assignment(selected, task))
                        minutes = task.start_time.hour*60 + task.start_time.minute + listOfAssignments[len(listOfAssignments)-1].nes_time
                        endOfTask = datetime.time(int(minutes/60), int(minutes) % 60)
                        ifAssigned = 1
                        # print(endOfTask)
                        tabooList1.append([driver, task.start_time, endOfTask])
                        break

            else:
                if task.start_time >= driver.shift and task.start_time <= driver.endTime:
                    selected = driver
                    if Assignment.Assignment(selected, task) in tabooAssignments:
                        continue
                    listOfAssignments.append(Assignment.Assignment(selected, task))
                    tabooList2.append([Assignment.Assignment(selected, task), period2])
                    tabooAssignments.append(Assignment.Assignment(selected, task))
                    minutes = task.start_time.hour * 60 + task.start_time.minute + listOfAssignments[len(listOfAssignments) - 1].nes_time
                    endOfTask = datetime.time(int(minutes / 60), int(minutes) % 60)
                    ifAssigned = 1
                    # print(endOfTask)
                    tabooList1.append([driver, task.start_time, endOfTask])
                    break
        if ifAssigned == 0:
            selected = helpDriver
            numberOfHelp+=1
            listOfAssignments.append(Assignment.Assignment(selected, task))

        unavailableToTask.clear()
    # print("==============================")
    # for assignment in listOfAssignments:
    #     assignment.show()

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
    listOfAssignments = []
    tabooList1.clear()
    tabooDriver.clear()
    percentageK0 = 0
    percentageK1 = 0
    percentageK2 = 0
    numberOfHelp = 0
    driversAfterHours = 0
    round += 1
print(tabooList3)
for element in tabooList3:
    for assignment in element:
        lista.append(assignment.driver.id +' => '+ assignment.task.strTask())

    print(lista)
combinations = lista.join('\n')
print(combinations)
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