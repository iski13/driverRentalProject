import Task,Place
def sortShort(listOfTasks):
    base = Place.Place()
    n = len(listOfTasks)
    while n > 0:
        for i in range (0, n-1):
            if listOfTasks[i].dest.dist(base) > listOfTasks[i+1].dest.dist(base):
                temp = listOfTasks[i]
                listOfTasks[i] = listOfTasks[i+1]
                listOfTasks[i+1] = temp
        n -= 1
    return listOfTasks

def sortLong(listOfTasks):
    base = Place.Place()
    n = len(listOfTasks)
    while n > 0:
        for i in range(0, n - 1):
            if listOfTasks[i].dest.dist(base) < listOfTasks[i + 1].dest.dist(base):
                temp = listOfTasks[i]
                listOfTasks[i] = listOfTasks[i + 1]
                listOfTasks[i + 1] = temp
        n -= 1
    return listOfTasks