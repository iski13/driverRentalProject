import Place, datetime
shifts = {"1": 8, "2": 10, "3": 16}
special = ["K!", 1, 20, 21, "1", 16, False]


class Driver():


    def __init__(self, id = 'K!',fulltimer = 0, salary = 20, extra_salary = 21.0, shift = '1', work_time = 16, ifextras = False):  #Tworzenie nowego kierowcy
        self.id = str(id)
        self.fulltimer = int(fulltimer)
        self.salary = int(salary)
        self.extra_salary = float(extra_salary)
        if self.fulltimer==1 :
            self.shift = datetime.time(shifts[shift],0)
        else :
            shift = shift.split(':')
            print(shift)
            self.shift = datetime.time(int(shift[0]), int(shift[1]))
        self.work_time = int(work_time)
        self.endTime = datetime.time(self.shift.hour + self.work_time, self.shift.minute)
        self.ifextras = bool(ifextras)
        self.position = Place.Place()

    def __init__(self, data = special):               # Inicjalizacja tabelą
        self.id = str(data[0])
        self.fulltimer = int(data[1])
        self.salary = int(data[2])
        self.extra_salary = float(data[3])
        if self.fulltimer == 1:
            self.shift = datetime.time(shifts[data[4]],0)
        else:
            data[4] = data[4].split(':')
            print(data[4])
            self.shift = datetime.time(int(data[4][0]),int(data[4][1]))
        self.work_time = int(data[5])
        if self.shift.hour + self.work_time >=24:
            self.endTime = self.endTime = datetime.time(23, 59)
        else:
            self.endTime = datetime.time(self.shift.hour + self.work_time, self.shift.minute)
        self.ifextras = int(data[6])
        self.position = Place.Place()

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False


   # def is_fulltimer(self):                                                        #Sprawdzanie etatu
   #     if self.fulltimer == True:
   #         return True
   #     else:
   #         return False

    def show(self):                                                                 #Prezentacja kierowcy
        print("Kierowca %s\t" % self.id)
        if(self.fulltimer==1):
            print("Pracownik etatowy\t")
            print("Pracuje od", self.shift.hour, ":", self.shift.minute,"przez", self.work_time, 'h za\t')
        else:
            print("Pracownik na zlecenie\t")
            print("Pracuje od", self.shift.hour, ":", self.shift.minute,"przez", self.work_time, 'h za\t')
        print(self.salary,"zl [ extra = ",self.extra_salary,"zl ]\t")
        if(self.ifextras==1):
            print("Nadgodziny możliwe\n")
        else:
            print("-\n")




#Testy

#a = Driver('K5',0,15,42,'13:40',4,1)
#a.show()
