import random, os

def generateTasks(n = random.randint(8,60)):
    # n = random.randint(8,15)
    # n = 100
    minuty = ["00","15","30","45"]
    path = os.getcwd()
    path = os.path.join(path, 'tasks.txt')
    exists = os.path.isfile(path)
    if not exists:
        for i in range(0, n):
            task = []
            task.append(str(random.randint(8, 23))+":"+minuty[random.randint(0, 3)])    #Losowanie godziny zlecenia
            task.append(str(random.randint(0, 1)))                                      #Losowanie typu zlecenia 1-podstawienie, 0-odbior
            task.append(str(random.randint(1, 5)))                                      #Losowanie miejsca realizacji zlecenia
            taskStr = "\t\t".join(task)
            file = open(path,'a')
            file.write(taskStr + "\n")
        file.close()
    else:
        print("Plik został już wygenerowany!\n")
    return