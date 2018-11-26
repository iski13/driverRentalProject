import random, os, Driver

path = os.getcwd()
path = os.path.join(path, 'drivers.txt')

file = open(path,'r')
drivers = file.read()
drivers = drivers.split("\n")
del drivers[len(drivers)-1]
for i in range(0,len(drivers)):
    drivers[i] = drivers[i].split("\t\t")
workers = Driver[drivers[0],drivers[1],drivers[2]]
for i in range(3,len(drivers)):
    workers.append(PartDriver)
print(workers)

#for i in range(0,num_of_drivers):
