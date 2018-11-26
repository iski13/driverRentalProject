import random, os

n = random.randint(8,15)
minuty = ["00","15","30","45"]
path = os.getcwd()
path = os.path.join(path, 'tasks.txt')

for i in range(0, n):
    task = []
    task.append(str(random.randint(8, 24))+":"+minuty[random.randint(0, 3)])    #Losowanie godziny zlecenia
    task.append(str(random.randint(0, 1)))                                      #Losowanie typu zlecenia 1-podstawienie, 0-odbior
    task.append(str(random.randint(1, 5)))                                      #Losowanie miejsca realizacji zlecenia
    taskStr = "\t\t".join(task)
    file = open(path,'a')
    file.write(taskStr + "\n")
    file.close()