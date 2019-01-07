import Driver, Task, datetime, Place
taskDuration = 15
std_velocity = 30

class Assignment():

    def __init__(self, driver, task):
        self.driver = driver
        self.task = task
        self.distance = driver.position.dist(task.dest)
        self.arrivalTime = (self.distance/std_velocity)*60  #Czas dojazdu do miejsca zlecenia w minutach
        self.returnToBaseTime = task.dest.dist(Place.Place("1"))/std_velocity*60   #Czas powrotu do bazy
        self.nes_time = self.arrivalTime + self.returnToBaseTime + taskDuration
        self.allowed = True

#    def __init__(self, other):
#        self.driver = other.driver
#        self.task = other.task
#        self.nes_time = other.nes_time

# Sprawdzanie równości kierowcy i tasku
    def is_same(self, other):
        if self.driver == other.driver and self.task == other.task:
            return True
        else:
            return False

# ----------
# Operatory:
# ----------

    def __eq__(self, other):  # Operator ==
        if self.is_same(other) and self.nes_time == other.nes_time:
            return True
        else:
            return False

    def __gt__(self, other):  # Operator >
        if self.is_same(other) and self.nes_time > other.nes_time:
            return True
        else:
            return False

    def __ge__(self, other):  # Operator >=
        if self.is_same(other) and self.nes_time >= other.nes_time:
            return True
        else:
            return False

    def __lt__(self, other):  # Operator <
        if self.is_same(other) and self.nes_time < other.nes_time:
            return True
        else:
            return False

    def __le__(self, other):  # Operator <=
        if self.is_same(other) and self.nes_time <= other.nes_time:
            return True
        else:
            return False



    #Wyswietlanie przypisania
    def show(self):
        print("Kierowca",self.driver.id,"\t-->")
        self.task.show()
        print("\t\tSzacowany czas:\t",datetime.time(int(self.nes_time/60),int(self.nes_time%60)))


#------
#Testy:
#------

#d = Driver.Driver()
#t = Task.Task()
#a = Assignment(d,t)
#a.show()
