import Driver, Task, datetime

std_velocity = 60

class Assignment():

    def __init__(self, driver, task, nes_time):
        self.driver = driver
        self.task = task
        if nes_time:
            self.nes_time = nes_time
        else:
            self.nes_time = (task.dest.dist(driver)/std_velocity)*2 + task.duration
        self.allowed = True

#    def __init__(self, other):
#        self.driver = other.driver
#        self.task = other.task
#        self.nes_time = other.nes_time

# ----------
# Operatory:
# ----------

    def __eq__(self, other):  # Operator ==
        if self.driver == other.driver and self.task == other.task and self.nes_time == other.nes_time:
            return True
        else:
            return False

    def __gt__(self, other):  # Operator >
        if self.driver == other.driver and self.task == other.task and self.nes_time > other.nes_time:
            return True
        else:
            return False

    def __ge__(self, other):  # Operator >=
        if self.driver == other.driver and self.task == other.task and self.nes_time >= other.nes_time:
            return True
        else:
            return False

    def __lt__(self, other):  # Operator <
        if self.driver == other.driver and self.task == other.task and self.nes_time < other.nes_time:
            return True
        else:
            return False

    def __le__(self, other):  # Operator <=
        if self.driver == other.driver and self.task == other.task and self.nes_time <= other.nes_time:
            return True
        else:
            return False

    # Sprawdzanie równości kierowcy i tasku
    def is_same(self, other):
        if self.driver == other.driver and self.task == other.task:
            return True
        else:
            return False
    #Wyswietlanie przypisania
    def show(self):
        print(self.driver.id,"\t-->")
        self.task.show()
        print("\t\tSzacowany czas:\t",datetime.time(int(self.nes_time/60),int(self.nes_time%60)))


#------
#Testy:
#------

#d = Driver.Driver()
#t = Task.Task()
#a = Assignment(d,t)
#a.show()