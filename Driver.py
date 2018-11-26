class Driver():
    def __init__(self,id = 0,fulltimer = True, salary = 14, extra_salary = 21.0, work_time = 8, ifextras = False):  #Tworzenie nowego kierowcy
        self.id = id
        self.fulltimer = fulltimer
        self.salary = salary
        self.extra_salary = salary * 1.5
        self.work_time = work_time
        self.ifextras = ifextras

#    def is_fulltimer(self):
#        if self.fulltimer == True:
#            return True
#        else:
#            return False

    def show(self):
        print("Kierowca %d\t" % self.id)
        if(self.fulltimer):
            print("etat\t")
        else:
            print("zlecenie\t")
        print(self.salary,'\t',self.extra_salary,'\t',self.work_time,'h\t')
        if(self.ifextras):
            print("nadgodziny możliwe\n")
        else:
            print("-\n")


class FullDriver(Driver):                                                           #Tworzenie kierowcy etatowego
    def __init__(self, shifts = 1):
        self.shifts = shifts

class PartDriver(Driver):                                                           #Tworzenie kierowcy dorywczego
    def __init__(self, start_time = 15.00):
        if self.work_time > 0 and self.work_time < 10:
            self.start_time = start_time
        else:
            print("Zbyt duży czas pracy! Rozważ zatrudnienie na etat!")
            self = Null
