import simpleNeighboursBeta, mergedTasksNeighbour, noReturnToBaseNeighbour, shortestTaskNeighbour

print('''Witaj!
Przed rozpoczęciem umieść pliki z zleceniami i dostępnymi kierowcami, których chesz przypisać.
Jeśli chcesz jedynie przetestować działanie aplikacji, niemusisz tego robić,
a pliki zostaną wygenerowane dla ciebie automatycznie. :D''')
input("Aby kontynuować wciśnij enter...")
print('''Nasza aplikacja posiada 5 typów sąsiedztw kolejnych rozwiązań, które mogą zwracać
różne wyniki po zakończeniu wykonywania. W celu najlepszego przeszukania polecamy przetestować
kilka różnych modułów programu w celu znalezienia rozwiązania najlepszego.
      
      1 - Proste przyporządkowanie, zlecenia wybierane w kolejności godzinowej, kierowca powraca do bazy po zleceniu.
      2 - Proste przyporządkowanie z łączonymi zleceniami podstawienie i odbiór.
      3 - Przyporządkowanie proste, jednak po zleceniu podstawienia kierowca oczekuje w miejscu podstawienia.
      4 - Przyporządkowanie w pierwszej kolejności krótkich zleceń dla kierowców etatowych.
      5 - Przyporządkowanie w pierwszej kolejności długich zleceń dla kierowców etatowych.
      ''')

typeOfNeighbours = input("Wybierz typ sąsiedztwa i wciśnij enter: ")
iterations = input("Podaj liczbę iteracji dla algorytmu: ")
tabooPeriod = input("Podaj okres zabronień dla danego przypisania: ")

if typeOfNeighbours == "1":
    simpleNeighboursBeta.simpleNeighbours(iterations, tabooPeriod)
elif typeOfNeighbours == "2":
    mergedTasksNeighbour.mergedNeighbours(iterations,tabooPeriod)
elif typeOfNeighbours == "3":
    noReturnToBaseNeighbour.noReturnNeighbours(iterations, tabooPeriod)
elif typeOfNeighbours == "4":
    shortestTaskNeighbour.shortestTaskFirstNeighbours(iterations, tabooPeriod, 1)
elif typeOfNeighbours == "5":
    shortestTaskNeighbour.shortestTaskFirstNeighbours(iterations, tabooPeriod, 0)
else:
    print("Nieprawidłowy typ zlecenia!!!")
