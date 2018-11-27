import random, os, Driver, Task, Place

#-----------------------------------------------
#Wczytanie z pliku do listy obiektow typu Driver

path = os.getcwd()
path = os.path.join(path, 'drivers.txt')
workers = [Driver]

file = open(path,'r')
drivers = file.read()
drivers = drivers.split("\n")
del drivers[len(drivers)-1]
#print(drivers)
for i in range(0,len(drivers)):
    drivers[i] = drivers[i].split("\t\t")
    #print(drivers[i])
    #drivers[i] = Driver(drivers[0])
    #dr = Driver(drivers)
#workers = Driver(workers)
#dr0 = workers[0]


#for i in range(0,len(drivers)):
#    workers.append(Driver(drivers[i]))

#workers[0].show()


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

#courses[i] = courses[i].split("\t\t")
#    courses[i][0] = courses[i][0].split(":")
#    courses[i][0][0] = int(courses[i][0][0])
#    courses[i][0][1] = int(courses[i][0][1])
#for i in range(0,len(courses)):
#    courses[i] = Task(time(courses[i][0][0],courses[i][0][1]),courses[i][1],courses[i][2])
#    tasks.append(t)
#for i in s:
#    h,m,t,d = s.split(' ')

print(s)