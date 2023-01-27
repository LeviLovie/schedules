import os
import sys
import json

# local UTC offset:
# int(datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset().seconds/3600)

schedule = []
path = ""
isDev = False

class User:
    nick: str
    timeZone: int
    minTime: int
    maxTime: int

    def __init__(self, data):
        self.nick = data['nick']
        self.timeZone = data['timeZone']
        self.minTime = data['minTime']
        self.maxTime = data['maxTime']

def openConfigFile():
    global schedule
    global path

    print("Files:")
    files = os.listdir("schedules")
    for i in files:
        if i == files[-1]:
            print("'" + i + "'")
        else:
            print("'" + i + "'", end=", ")
    print()
    
    path = "schedules/" + input("Enter name of schedule file (without `.json`): ") + ".json"
    try:
        with open(path) as json_file:
            schedule_json = json.load(json_file)
            schedule = [User(u) for u in schedule_json]
    except FileNotFoundError:
        print("File not found")
        return
    
    workOnSchedule()

def newConfigFile():
    name = "schedules/" + input("Enter name of schedule file (without `.json`): ") + ".json"

    with open(name, 'w') as outfile:
        json.dump([], outfile)
    
    clearTerminal()
    main()

def clearTerminal():
    global isDev
    print("\033c", end="")
    if isDev: print("\033[1;33mRunning in dev mode\033[0m")

def workWithInputForSchedule():
    print()
    print("1: Add user")
    print("2: Remove user")
    print("3: Change user")
    print("4: Save")
    print("5: Exit to menu")
    print("6: Full exit")
    print()
    inputData = int(input("Enter your choice: "))

    if inputData == 1:
        clearTerminal()

        print("Users:")
        for i in schedule:
            if i == schedule[-1]:
                print("'" + i.nick + "'")
            else:
                print("'" + i.nick + "'", end=", ")

        name = input("Type name of user: ")
        timeZone = int(input("Type time zone of user (UTC+): "))
        minTime = int(input("Type min time of user: "))
        maxTime = int(input("Type max time of user: "))
        schedule.append(User({
            "nick": name,
            "timeZone": timeZone,
            "minTime": minTime,
            "maxTime": maxTime
        }))

        workOnSchedule()
    elif inputData == 2:
        clearTerminal()

        print("Users:")
        for i in schedule:
            if i == schedule[-1]:
                print("'" + i.nick + "'")
            else:
                print("'" + i.nick + "'", end=", ")

        name = input("Type name of user: ")
        for i in schedule:
            if i.nick == name:
                schedule.remove(i)
                break

        workOnSchedule()
    elif inputData == 3:
        clearTerminal()

        print("Users:")
        for i in schedule:
            if i == schedule[-1]:
                print("'" + i.nick + "'")
            else:
                print("'" + i.nick + "'", end=", ")

        name = input("Type name of user: ")
        
        print("1: Change name")
        print("2: Change time zone")
        print("3: Change min time")
        print("4: Change max time")
        print("5: Change all")
        print("6: Exit")
        print()
        inputData = int(input("Enter your choice: "))
        if inputData == 1:
            newName = input("Type new name of user: ")
            for i in schedule:
                if i.nick == name:
                    i.nick = newName
                    break
        elif inputData == 2:
            newTimeZone = int(input("Type new time zone of user (UTC+): "))
            for i in schedule:
                if i.nick == name:
                    i.timeZone = newTimeZone
                    break
        elif inputData == 3:
            newMinTime = int(input("Type new min time of user: "))
            for i in schedule:
                if i.nick == name:
                    i.minTime = newMinTime
                    break
        elif inputData == 4:
            newMaxTime = int(input("Type new max time of user: "))
            for i in schedule:
                if i.nick == name:
                    i.maxTime = newMaxTime
                    break
        elif inputData == 5:
            newName = input("Type new name of user: ")
            newTimeZone = int(input("Type new time zone of user (UTC+): "))
            newMinTime = int(input("Type new min time of user: "))
            newMaxTime = int(input("Type new max time of user: "))
            for i in schedule:
                if i.nick == name:
                    i.nick = newName
                    i.timeZone = newTimeZone
                    i.minTime = newMinTime
                    i.maxTime = newMaxTime
                    break
        elif inputData == 6:
            clearTerminal()
            workOnSchedule()
            return

        workOnSchedule()
    elif inputData == 4:
        clearTerminal()

        with open(path, 'w') as outfile:
            json.dump([u.__dict__ for u in schedule], outfile)

        workOnSchedule()
    elif inputData == 5:
        clearTerminal()
        main()
    elif inputData == 6:
        clearTerminal()
        exit(0)
    else:
        clearTerminal()
        print("Invalid input")
        workOnSchedule()

def workOnSchedule():
    global schedule
    clearTerminal()

    print("+", end="")
    for i in range(20):
        print("-", end="")
    print("+", end="")
    for i in range((24 * 3) + 1):
        print("-", end="")
    print("+")

    print("|", end="")
    print("\033[1;32m" + "Name".center(20) + "\033[1;0m", end="")
    print("|", end="")
    print("\033[1;36m@\033[1;32m00000000011111111112222\033[1;0m", end="")
    print("\033[1;36m@\033[1;32m00000000011111111112222\033[1;0m", end="")
    print("\033[1;36m@\033[1;32m00000000011111111112222\033[1;36m@\033[1;0m|")

    print("|", end="")
    print("".center(20), end="")
    print("|", end="")
    print("\033[1;36m@\033[1;32m12345678901234567890123\033[1;0m", end="")
    print("\033[1;36m@\033[1;32m12345678901234567890123\033[1;0m", end="")
    print("\033[1;36m@\033[1;32m12345678901234567890123\033[1;36m@\033[1;0m|")

    print("+", end="")
    print("--------------------".center(20), end="")
    print("+", end="")
    for i in range((24 * 3) + 1):
        print("-", end="")
    print("+")

    for i in schedule:
        print("|", end="")
        print("\033[1;32m" + i.nick.center(20) + "\033[1;0m", end="")
        print("|", end="")

        for j in range((24 * 3) + 1):
            if j == 0 or j == 24 or j == 48 or j == 72:
                print("\033[1;36m@\033[1;0m", end="")
            else:
                if j >= (i.minTime + i.timeZone) and j < (i.maxTime + i.timeZone):
                    print("\033[1;32m#\033[1;0m", end="")
                elif j >= ((i.minTime + i.timeZone) - 24) + 1 and j < ((i.maxTime + i.timeZone) - 24):
                    print("\033[1;32m#\033[1;0m", end="")
                
                elif j >= (i.minTime + i.timeZone) + 24 and j < (i.maxTime + i.timeZone) + 24:
                    print("\033[1;32m#\033[1;0m", end="")
                elif j >= ((i.minTime + i.timeZone) - 24) + 25 and j < ((i.maxTime + i.timeZone) - 24) + 24:
                    print("\033[1;32m#\033[1;0m", end="")
                
                elif j >= (i.minTime + i.timeZone) + 48 and j < (i.maxTime + i.timeZone) + 48:
                    print("\033[1;32m#\033[1;0m", end="")
                elif j >= ((i.minTime + i.timeZone) - 24) + 48 and j < ((i.maxTime + i.timeZone) - 24) + 48:
                    print("\033[1;32m#\033[1;0m", end="")
                
                else:
                    print("\033[1;32m.\033[1;0m", end="")
        
        print("|")
    
    print("+", end="")
    for i in range(20):
        print("-", end="")
    print("+", end="")
    for i in range((24 * 3) + 1):
        print("-", end="")
    print("+")

    workWithInputForSchedule()    

def main():
    print("1: Open config file (schedule file)")
    print("2: New config file (schedule file)")
    print("3: Exit")
    print()
    inputData = int(input("Enter your choice: "))
    
    if inputData == 1:
        clearTerminal()
        openConfigFile()
    elif inputData == 2:
        clearTerminal()
        newConfigFile()
    elif inputData == 3:
        clearTerminal()
        exit(0)
    else:
        clearTerminal()
        print("Invalid input")
        return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--dev":
            isDev = True

    clearTerminal()
    print("\033[1;33mYour size of terminal have to be biger, tht 175:25\033[0m")
    main()