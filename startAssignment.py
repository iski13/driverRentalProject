import Driver, Task, Assignment, Place, datetime
tabooList1 = []
tabooDriver = []
availableDriversTime = []
availableDriversReal = []
listOfAssignments = []

def startAssignment(drivers, tasks, helpDriver):
    driversAfterHours = 0


    for hour in range (8, 24):
        for minute in range (0,60):
            for driver in tabooList1 :
                driver[1] -= 1
                if driver[1] == 0:
                    tabooList1.remove(driver)
                    tabooDriver.remove(driver[0])
                    if (hour > driver[0].shift.hour + driver[0].work_time) or (hour == driver[0].shift.hour + driver[0].work_time and minute > driver[0].shift.minute):
                        driversAfterHours += 1

            for driver in drivers:
                if driver.fulltimer == 0:
                    if driver.shift.hour == hour and driver.shift.minute == minute :
                        availableDriversTime.append(driver)
                        availableDriversReal.append(driver)
                        #print("Zaczyna")

                    if (driver in tabooDriver)==False and (driver in availableDriversTime) and (driver in availableDriversReal)==False :
                        availableDriversReal.append(driver)
                        # print("Odzabroniony")

                    if ((driver.shift.hour+driver.work_time == hour) and (driver.shift.minute == minute)) and (driver in availableDriversTime) :
                        availableDriversTime.remove(driver)
                        if driver in availableDriversReal :
                            availableDriversReal.remove(driver)
                        #print("zakonczyl")

            for task in tasks:
                minutes = int(task.dest.dist(Place.Place("1")) / Assignment.std_velocity * 60)  # Czas dojazdu od bazy

                if task.start_time.minute - minutes < 0:  # Deklaracja rzeczywistej godziny rozpoczęcia
                    taskStart = datetime.time(task.start_time.hour - 1, 59 + task.start_time.minute - minutes)
                else:
                    taskStart = datetime.time(task.start_time.hour, task.start_time.minute - minutes)
                if taskStart.hour == hour and taskStart.minute == minute:
                    # task.show()
                    if availableDriversReal:
                        for driver in availableDriversReal:
                            # if tabooAssignments:

                            minDistance = driver.position.dist(task.dest)
                            selected = driver
                            break
                    else:
                        selected = helpDriver
                    listOfAssignments.append(Assignment.Assignment(selected, task))

    return listOfAssignments