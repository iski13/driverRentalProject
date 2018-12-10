import datetime, Place

class Task():

    def __init__(self, start_timeH=18, start_timeM=0, tasktype = 1, dest = 0):            #Inicjalizacja zadania
        self.start_time = datetime.time(int(start_timeH), int(start_timeM))
        self.tasktype = int(tasktype)
        self.dest = Place.Place(dest)

    def __init__(self, data):                                                             #Inicjalizacja zadania przez listę danych
        self.start_time = datetime.time(int(data[0]), int(data[1]))
        self.tasktype = int(data[2])
        self.dest = Place.Place(data[3])

    def show(self):                                                                 #Prezentacja zadania przez print
        if self.tasktype==1:
            return print("Dostarczenie na\t",self.start_time,"\tz\t",self.dest.name)
        else:
            return print("Odebranie o\t\t",self.start_time,"\tz\t",self.dest.name)

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
    # def __eq__(self, other):            #Operator '=='
    #     if self.start_time == other.start_time:
    #         return True
    #     else:
    #         return False


#Testy
