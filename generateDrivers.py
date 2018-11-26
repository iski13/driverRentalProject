import random, os

n = random.randint(3,10)                                    #Losowanie liczby kierowców dostepnych danego dnia

path = os.getcwd()                                          #Ustawienie ściezki do pliku na bieżący folder
path = os.path.join(path, 'drivers.txt')                    #Ustalenie nazwy pliku do zapisu

salary = int(input("Podaj podstawowe wynagrodzenie: "))     #Wprowadznie kwoty wynagrodzenia godzinowego dla kierowców
zmiany = [1, 2, 3]                                          #Numery zmian etatowych (rozszyfrowanie w głównym programie)
random.shuffle(zmiany)                                      #Wymieszanie kolejności

for i in range(0, n):
    driver = []                                             #Pusta lista gdzie przechowujemy dane o generowanym kierowcy
    driver.append("K%d" % i)
    if i < 3:
        driver.append("1")                                  #Typ zatrudnienia kierowcy 1-etat, 0-dorywczy
    else:
        driver.append('0')
    driver.append(str(salary))
    driver.append(str(1.5* salary))                         #Wynagrodzenie dodatkowe 150% podstawowego
    if i == 0 or i == 1 or i == 2:
        driver.append(str(zmiany.pop()))
        driver.append("8")
    else:
        driver.append(str(random.randint(8,23))+":"+str(random.randint(0,59)))      #Losowanie czasu dostępności dodatkowej
        driver.append(str(random.randint(1,10)))            #Losowanie czasu dostępności
    driver.append(str(random.randint(0,1)))                 #Losowa zgoda na nadgodziny 1-tak, 2-nie

    driverStr = "\t\t".join(driver)                         #Zmiana listy na string
    with open(path,'a') as file:
        file.write(driverStr + '\n')
        file.write('\n')
