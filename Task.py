import datetime

class Task():

    def __init__(self, start_time = time(18,0), tasktype = 1, dest = Place()):            #Inicjalizacja zadania
        self.start_time = start_time
        self.tasktype = tasktype
        self.dest = dest

    def show(self):                                                                 #Prezentacja zadania
        if self.tasktype==1:
            return print("Dostarczenie na\t",self.start_time,"\tz\t",self.dest.name)
        else:
            return print("Odebranie o\t\t",self.start_time,"\tz\t",self.dest.name)


#Testy

#p = Place('Zoo',25,75,time(1,5),time(2,4))
#a = Task(time(17,45), 0, p)
#a.show()
#a = Task(time(13,43))
#a.show()