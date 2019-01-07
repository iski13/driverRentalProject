import os, Task
from generateTasks import generateTasks



#-----------------------------------------------
#Wczytywanie z pliku do listy obiektow typu Task

listOfTasks = []
courses = []
s = []

path = os.getcwd()
path = os.path.join(path, 'tasks.txt')
file = open(path,'r')
courses = file.read()
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
file.close()
listOfTasks.sort()
for i in range(0, len(listOfTasks)):
    listOfTasks[i].show()                                  #Sortowanie zlecen wedlug godziny

merged = []
#Laczenie przeczytanych taskow
for i in range(0, len(listOfTasks)):
    for j in range(0, len(listOfTasks)):
        if (listOfTasks[i].tasktype != listOfTasks[j].tasktype) and listOfTasks[i].dest == listOfTasks[j].dest and (listOfTasks[j].start_time - listOfTasks[i].start_time) <  01.00 and (listOfTasks[j].start_time - listOfTasks[i].start_time) > 00.15 and i != j :
            new_task = Task(listOfTasks[i].start_time.hour, listOfTasks[i].start_time.minutes, 2, listOfTasks[i].dest ,(listOfTasks[i].duration + listOfTasks[j].duration + (listOfTasks[j].start_time - listOfTasks[i].start_time)))
            merged.append(new_task)
            del listOfTasks[i]
            del listOfTasks[j]
        else:
            continue
for i in range(0, len(listOfTasks)):
    merged.append(listOfTasks[i])




#Tworzenie nowego pliky z taskami i zapis do niego

path2 = os.getcwd()
path2 = os.path.join(path2, 'tasks_merged.txt')
file = open(path,'r')

