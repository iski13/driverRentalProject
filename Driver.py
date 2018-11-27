class Driver():


    def __init__(self,id = 'K0',fulltimer = True, salary = 14, extra_salary = 21.0, shift = 1, work_time = 8, ifextras = False):  #Tworzenie nowego kierowcy
        self.id = str(id)
        self.fulltimer = bool(fulltimer)
        self.salary = int(salary)
        self.extra_salary = salary * 1.5
        self.shift = str(shift)
        self.work_time = int(work_time)
        self.ifextras = bool(ifextras)

#    def is_fulltimer(self):                                                        #Sprawdzanie etatu
#        if self.fulltimer == True:
#            return True
#        else:
#            return False

    def show(self):                                                                 #Prezentacja kierowcy
        print("Kierowca %s\t" % self.id)
        if(self.fulltimer):
            print("Pracownik etatowy\t")
            print("Pracuje", self.work_time,'h za\t')
        else:
            print("Pracownik na zlecenie\t")
            print("Pracuje od", self.shift,'za\t')
        print(self.salary,"zl [ extra = ",self.extra_salary,"zl ]\t")
        if(self.ifextras):
            print("Nadgodziny możliwe\n")
        else:
            print("-\n")

#    def __init__(self, *data):                                                     #INicjalizacja tabelą
#        self.id = str(data[1])
#        self.fulltimer = bool(data[2])
#        self.salary = int(data[3])
#        self.extra_salary = self.salary * 1.5
#        self.shift = str(data[5])
#        self.work_time = int(data[6])
#        self.ifextras = bool(data[7])


#Testy

#a = Driver('K5',0,15,42,'13:40',4,1)
#a.show()
