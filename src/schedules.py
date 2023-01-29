from . import db
from . import schedulesFoo as SFoo
from . import foo


def open_schedule(isDev, name):
    foo.clearTerminal(isDev)
    print(foo.COLOR_CYAN + "Schedule" + foo.COLOR_RESET)

    SFoo.printHeader()
    schedules = db.get_schedules(db.open_db())
    schedule = None
    for i in schedules:
        if i["name"] == name:
            schedule = i
            break
    usersInThisSchedule = db.get_usersInSchedule(db.open_db(), name)

    for i in range(len(usersInThisSchedule)):
        toPrint = "|" + foo.COLOR_GREEN + (usersInThisSchedule[i].center(20)) + foo.COLOR_RESET + "|"
        for j in range(24 * 2 + 1):
            user = db.get_user(db.open_db(), usersInThisSchedule[i])
            if j == 0 or j == 24 or j == 48:
                toPrint += foo.COLOR_CYAN + "@" + foo.COLOR_RESET
            
            elif j >= (user.minTime + user.timeZone) - 24 and j < (user.maxTime + user.timeZone) - 24:
                toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            elif j >= (user.minTime + user.timeZone) and j < (user.maxTime + user.timeZone):
                toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            elif j >= (user.minTime + user.timeZone) + 24 and j < (user.maxTime + user.timeZone) + 24:
                toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            
            # elif j >= (user.minTime + user.timeZone) and j < (user.maxTime + user.timeZone):
            #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            # elif j >= (user.minTime + user.timeZone) + 24 and j < (user.maxTime + user.timeZone) + 24:
            #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            
            # elif j >= (user.minTime + user.timeZone) + 24 and j < (user.maxTime + user.timeZone) + 24:
            #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            # elif j >= ((user.minTime + user.timeZone) - 24) + 25 and j < ((user.maxTime + user.timeZone) - 24) + 24:
            #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            
            # elif j >= (user.minTime + user.timeZone) + 48 and j < (user.maxTime + user.timeZone) + 48:
            #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
            
            else:
                toPrint += foo.COLOR_GREEN + "." + foo.COLOR_RESET
        toPrint += "|"
        # user = db.get_user(db.open_db(), usersInThisSchedule[i])
        #                 # toPrint += foo.COLOR_GREEN + str(SFoo.firstTimeSymols[j]) + foo.COLOR_RESET

        # if j >= (user.minTime + user.timeZone) and j < 24:
        #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
        # # elif j >= (user.minTime + user.timeZone) + 1 and j < 24:
        # #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
        
        # # elif j >= (user.minTime + user.timeZone) + 24 and j < (user.maxTime + user.timeZone) + 24:
        # #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
        # # elif j >= ((user.minTime + user.timeZone) - 24) + 25 and j < ((user.maxTime + user.timeZone) - 24) + 24:
        # #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET

        # else:
        #     toPrint += foo.COLOR_GREEN + "." + foo.COLOR_RESET
        

                        # if j >= (i.minTime + i.timeZone) and j < (i.maxTime + i.timeZone):
                        #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
                        # elif j >= ((i.minTime + i.timeZone) - 24) + 1 and j < ((i.maxTime + i.timeZone) - 24):
                        #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
                        
                        # elif j >= (i.minTime + i.timeZone) + 24 and j < (i.maxTime + i.timeZone) + 24:
                        #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
                        # elif j >= ((i.minTime + i.timeZone) - 24) + 25 and j < ((i.maxTime + i.timeZone) - 24) + 24:
                        #     toPrint += foo.COLOR_GREEN + "#" + foo.COLOR_RESET
        print(toPrint)
    SFoo.printBottom()
    print()

    print("1. Add User")
    print("2. Delete User")
    print("5. Back")
    print()
    try:
        chose = int(input("Enter your choice: "))
    except ValueError:
        foo.clearTerminal(isDev)
        print(foo.COLOR_YELLOW + "Invalid input" + foo.COLOR_RESET)
        open_schedule(isDev, name)
    if chose == 1:
        foo.clearTerminal(isDev)
        result = SFoo.add_user(isDev, name)
        if result == 0:
            foo.clearTerminal(isDev)
            open_schedule(isDev, name)
        else:
            foo.clearTerminal(isDev)
            print(foo.COLOR_YELLOW + "It's with unknow error, please, see, did you it correct" + foo.COLOR_RESET)
            open_schedule(isDev, name)
    elif chose == 2:
        foo.clearTerminal(isDev)
        result = SFoo.delete_user(isDev, name)
        if result == 0:
            foo.clearTerminal(isDev)
            open_schedule(isDev, name)
        else:
            foo.clearTerminal(isDev)
            print(foo.COLOR_YELLOW + "It's with unknow error, please, see, did you it correct" + foo.COLOR_RESET)
            open_schedule(isDev, name)
    elif chose == 5:
        foo.clearTerminal(isDev)
        return 0
    return 0


def general(isDev):
    print(foo.COLOR_CYAN + "Schedules" + foo.COLOR_RESET)
    schedules = db.get_schedules(db.open_db())
    SFoo.print_schedules(schedules)
    print()
    print("1. Add Schedule")
    print("2. Delete Schedule")
    print("3. Open Schedule")
    print("5. Back")
    print()

    try:
        chose = int(input("Enter your choice: "))
    except ValueError:
        foo.clearTerminal(isDev)
        print(foo.COLOR_YELLOW + "Invalid input" + foo.COLOR_RESET)
        general(isDev)
    
    if chose == 1:
        foo.clearTerminal(isDev)
        result = SFoo.add_schedule(isDev)
        if result == 0: 
            foo.clearTerminal(isDev)
            general(isDev)
        else:
            foo.clearTerminal(isDev)
            print(foo.COLOR_YELLOW + "It's with unknow error, please, see, did you it correct" + foo.COLOR_RESET)
            general(isDev)
    elif chose == 2:
        foo.clearTerminal(isDev)
        result = SFoo.delete_schedule(isDev)
        if result == 0:
            foo.clearTerminal(isDev)
            general(isDev)
        else:
            foo.clearTerminal(isDev)
            print(foo.COLOR_YELLOW + "It's with unknow error, please, see, did you it correct" + foo.COLOR_RESET)
            general(isDev)
    elif chose == 3:
        foo.clearTerminal(isDev)
        name = input("Enter schedule name: ")
        result = open_schedule(isDev, name)
        if result == 0:
            foo.clearTerminal(isDev)
            general(isDev)
        else:
            foo.clearTerminal(isDev)
            print(foo.COLOR_YELLOW + "It's with unknow error, please, see, did you it correct" + foo.COLOR_RESET)
            general(isDev)
    elif chose == 5:
        foo.clearTerminal(isDev)
        return 0
    else:
        foo.clearTerminal(isDev)
        print(foo.COLOR_YELLOW + "Invalid input" + foo.COLOR_RESET)
        general(isDev)