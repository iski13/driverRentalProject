import os, Task

def mergeTasks(listOfTasks):
        #Laczenie przeczytanych taskow
        merged = []
        mergedListOfTasks = []

        # for i in range(0, len(listOfTasks)):
        #     for j in range(0, len(listOfTasks)):
        #         if (listOfTasks[i].tasktype != listOfTasks[j].tasktype) and listOfTasks[i].dest == listOfTasks[j].dest and (listOfTasks[j].start_time - listOfTasks[i].start_time) <  01.00 and (listOfTasks[j].start_time - listOfTasks[i].start_time) > 00.15 and i != j :
        #             new_task = Task.Task(listOfTasks[i].start_time.hour, listOfTasks[i].start_time.minutes, 2, listOfTasks[i].dest)
        #             merged.append(new_task)
        #             del listOfTasks[i]
        #             del listOfTasks[j]
        #         else:
        #             continue
        # for i in range(0, len(listOfTasks)):
        #     merged.append(listOfTasks[i])

        for i in range(0,len(listOfTasks)):
            for j in range(0, len(listOfTasks)):
                if listOfTasks[i].tasktype == 1 and listOfTasks[j].tasktype == 0 and listOfTasks[i].dest == listOfTasks[j].dest:
                    if (((listOfTasks[j].start_time.hour - listOfTasks[i].start_time.hour)*60 + (listOfTasks[j].start_time.minute - listOfTasks[i].start_time.minute)) <= 60) and (((listOfTasks[j].start_time.hour - listOfTasks[i].start_time.hour)*60 + (listOfTasks[j].start_time.minute - listOfTasks[i].start_time.minute)) > 15):
                        if not listOfTasks[i] in merged and not listOfTasks[j] in merged:
                            newTask = Task.Task(listOfTasks[i].start_time.hour, listOfTasks[i].start_time.minute, 2, listOfTasks[i].dest.spotNumber, listOfTasks[j].start_time.hour, listOfTasks[j].start_time.minute)
                            mergedListOfTasks.append(newTask)
                            merged.append(listOfTasks[i])
                            merged.append(listOfTasks[j])

                else:
                    continue

        for merge in merged:
            merge.show()
            listOfTasks.remove(merge)

        for task in listOfTasks:
            mergedListOfTasks.append(task)

        mergedListOfTasks.sort()
        # Tworzenie nowego pliku z taskami i zapis do niego
        # path2 = os.getcwd()
        # path2 = os.path.join(path2, 'tasks_merged.txt')
        # file = open(path2, 'w')
        # for task in merged:
        #     table = []
        #     table.append(str(task.start_time))
        #     table.append(str(task.tasktype))
        #     table.append(str(task.dest))
        #     tableStr = "\t\t".join(table)
        # file.write(tableStr + "\n")
        # file.close()
        return mergedListOfTasks