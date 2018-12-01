import Place

class Driver():


    def __init__(self,id = 'K0',fulltimer = True, salary = 14, extra_salary = 21.0, shift = 1, work_time = 8, ifextras = False):  #Tworzenie nowego kierowcy
        self.id = str(id)
        self.fulltimer = int(fulltimer)
        self.salary = int(salary)
        self.extra_salary = float(extra_salary)
        self.shift = str(shift)
        self.work_time = int(work_time)
        self.ifextras = bool(ifextras)
        self.position = Place.Place()

    def __init__(self, data):               # Inicjalizacja tabelą
        self.id = str(data[0])
        self.fulltimer = int(data[1])
        self.salary = int(data[2])
        self.extra_salary = float(data[3])
        self.shift = str(data[4])
        self.work_time = int(data[5])
        self.ifextras = int(data[6])
        self.position = Place.Place()


#    def is_fulltimer(self):                                                        #Sprawdzanie etatu
#        if self.fulltimer == True:
#            return True
#        else:
#            return False

    def show(self):                                                                 #Prezentacja kierowcy
        print("Kierowca %s\t" % self.id)
        if(self.fulltimer==1):
            print("Pracownik etatowy\t")
            print("Pracuje", self.work_time,'h za\t')
        else:
            print("Pracownik na zlecenie\t")
            print("Pracuje od", self.shift,'za\t')
        print(self.salary,"zl [ extra = ",self.extra_salary,"zl ]\t")
        if(self.ifextras==1):
            print("Nadgodziny możliwe\n")
        else:
            print("-\n")




#Testy

#a = Driver('K5',0,15,42,'13:40',4,1)
#a.show()
