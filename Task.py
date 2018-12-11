import datetime, Place

BasicErrandTime = 15

class Task():


    def __init__(self, start_timeH=18, start_timeM=0, tasktype = 1, dest = 0):              #Inicjalizacja zadania
        self.start_time = datetime.datetime(13,1,19,int(start_timeH), int(start_timeM))
        self.tasktype = int(tasktype)
        self.dest = Place.Place(dest)
        self.duration = BasicErrandTime


    def __init__(self, data):                                                               #Inicjalizacja zadania przez liste danych
        self.start_time = datetime.datetime(13,1,19,int(data[0]), int(data[1]))
        self.tasktype = data[2]
        self.dest = Place.Place(int(data[3]))
        self.duration = BasicErrandTime

# Wyswietlanie
    def show(self):                                                                         #Prezentacja zadania przez print
        if self.tasktype == 1:
            return print("Dostarczenie na\t",self.start_time.time(),"\tdo\t",self.dest.name)
        elif self.tasktype == 0:
            return print("Odebranie o\t\t",self.start_time.time(),"\tz\t",self.dest.name)
        else:
            return print("Dostarczenie na\t",self.start_time.time(),"\ti odebranie o\t",(self.start_time + datetime.timedelta(1, self.duration - BasicErrandTime)).time(),"\tz\t", self.dest.name)



# Operatory porownania czasu
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


    def __eq__(self, other):
        if self.dest == other.dest and self.start_time == other.start_time and self.tasktype == other.tasktype:
            return True
        else:
            return False

    def is_same_type(self, other):
        if self.tasktype == other.tasktype :
            return True
        else:
            return False

    def __add__(self, other):                                                                                               # Laczenie taskow w jeden
        if not self.is_same_type(other) and self == other and 00.15 < abs(self.start_time - other.start_time) < 01.00 :     # Sprawdzenie, czy taski sa roznych typow, czy maja taki sam dest
                                                                                                                            # i czy roznica miedzy ich czasami jest satysfakcjonujaca
            if self.tasktype != 2 and other.tasktype != 2 :                                                                 # Sprawdzenie, czy task nie jest juz polaczony
                self.duration = 2 * BasicErrandTime + abs(self.start_time - other.start_time)
                self.tasktype = 2
                self.start_time = self.start_time if self <= other else other.start_time
                return self
            else:
                return self

        else:
            return self



#Testy
