import datetime, Place

class Task():

    def __init__(self, start_timeH=18, start_timeM=0, tasktype = 1, dest = "0", start_timeH2=1, start_timeM2=1):            #Inicjalizacja zadania
        self.start_time = datetime.time(int(start_timeH), int(start_timeM))
        self.tasktype = int(tasktype)
        self.dest = Place.Place(dest)
        if self.tasktype == 2:
            self.start_time2 = datetime.time(int(start_timeH2), int(start_timeM2))

    # def __init__(self, data, start_timeH2=1, start_timeM2=1):                                                             #Inicjalizacja zadania przez listę danych
    #     self.start_time = datetime.time(int(data[0]), int(data[1]))
    #     self.tasktype = int(data[2])
    #     self.dest = Place.Place(data[3])
    #     if self.tasktype == 2:
    #         self.start_time2 = datetime.time(int(start_timeH2), int(start_timeM2))

    def strTask(self):
        if self.tasktype == 1:
            string = "Dostarczenie na "+ str(self.start_time)+" z "+str(self.dest.name)
        elif self.tasktype == 0:
            string = "Odebranie o "+str(self.start_time)+" z "+str(self.dest.name)
        return string
    def show(self):                                                                 #Prezentacja zadania przez print
        if self.tasktype == 1:
            return print("Dostarczenie na\t",self.start_time,"\tz\t",self.dest.name)
        elif self.tasktype == 0:
            return print("Odebranie o\t\t",self.start_time,"\tz\t",self.dest.name)
        else:
            return print("Dostarczenie na\t",self.start_time, "\ti odbiór o\t", self.start_time2, "\tz\t",self.dest.name)

    def __gt__(self, other):            #Operator '>'
        if self.start_time > other.start_time :
            return True
        else:
            return False

    def __lt__(self, other):            #Operator '<'
        if self.start_time < other.start_time :
            return True
        else:
            return False

    def __le__(self, other):            #Operator '<='
        if self.start_time<=other.start_time:
            return True
        else:
            return False

    def __ge__(self, other):            #Operator '>='
        if self.start_time>=other.start_time:
            return True
        else:
            return False
    def __eq__(self, other):            #Operator '=='
        if self.start_time == other.start_time and self.dest == other.dest and self.tasktype == other.tasktype:
            return True
        else:
            return False
