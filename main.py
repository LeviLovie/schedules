import sys
import json

# local UTC offset:
# int(datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset().seconds/3600)

schedule = {}
isDev = False


class User:
    nick: str
    timeZone: int
    minTime: int
    maxTime: int

    def __init__(self, nick, timeZone, minTime, maxTime):
        self.nick = nick
        self.timeZone = timeZone
        self.minTime = minTime
        self.maxTime = maxTime


def clearTerminal():
    global isDev
    print("\033c", end="")
    if isDev: print("\033[1;33mRunning in dev mode\033[0m")

def printSchedule():
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

    print("|", end="")
    print("--------------------".center(20), end="")
    print("+", end="")
    for i in range((24 * 3) + 1):
        print("-", end="")
    print("|")

    for i in schedule:
        print("|", end="")
        print("\033[1;32m" + i["nick"].center(20) + "\033[1;0m", end="")
        print("|", end="")

        for j in range((24 * 3) + 1):
            if j == 0 or j == 24 or j == 48 or j == 72:
                print("\033[1;36m@\033[1;0m", end="")
            else:
                if j >= (i["minTime"] + i["timeZone"]) and j < (i["maxTime"] + i["timeZone"]):
                    print("\033[1;32m#\033[1;0m", end="")
                elif j >= ((i["minTime"] + i["timeZone"]) - 24) + 1 and j < ((i["maxTime"] + i["timeZone"]) - 24):
                    print("\033[1;32m#\033[1;0m", end="")
                
                elif j >= (i["minTime"] + i["timeZone"]) + 24 and j < (i["maxTime"] + i["timeZone"]) + 23:
                    print("\033[1;32m#\033[1;0m", end="")
                elif j >= ((i["minTime"] + i["timeZone"]) - 24) + 25 and j < ((i["maxTime"] + i["timeZone"]) - 24) + 23:
                    print("\033[1;32m#\033[1;0m", end="")
                
                elif j >= (i["minTime"] + i["timeZone"]) + 49 and j < (i["maxTime"] + i["timeZone"]) + 48:
                    print("\033[1;32m#\033[1;0m", end="")
                elif j >= ((i["minTime"] + i["timeZone"]) - 24) + 50 and j < ((i["maxTime"] + i["timeZone"]) - 24) + 48:
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
            
            # if j >= i["minTime"] and j <= i["maxTime"]:
            #     print("#", end="")
            # else:
            #     print("i", end="")
            
            # if j <= 24:
            #     if (j + i["timeZone"] >= i["minTime"] and j + i["timeZone"] <= i["maxTime"] + i["timeZone"]):
            #         print("#", end="")
            #     else:
            #         print("i", end="")
            
            # if j <= 24 * 2 and j >= 24:
            #     if (j - i["timeZone"] >= i["minTime"] + 24 and j - i["timeZone"] <= i["maxTime"] - i["timeZone"] + 24):
            #         print("#", end="")
            #     else:
            #         print("i", end="")
            
            # elif j <= 24 * 3:
            #     if (j + i["timeZone"] >= i["minTime"] + (24 * 2) and j + i["timeZone"] <= i["maxTime"] + i["timeZone"] + (24 * 2)):
            #         print("#", end="")
            #     else:
            #         print("i", end="")

            # if j == 0 or j == 24 or j == 48:
            #     print("@", end="")
        # for j2 in range(24):
        #     print("  ", end="")
        # print("|", end="")
        # for j3 in range(24):
        #     print("  ", end="")
        # print("|  ", end="")

def openConfigFile():
    global schedule
    
    path = "schedules/" + input("Enter name of schedule file (without `.json`): ") + ".json"
    try:
        with open(path) as json_file:
            schedule = json.load(json_file)
    except FileNotFoundError:
        print("File not found")
        return
    
    printSchedule()

def newConfigFile():
    print("New config file")

def main():
    print("1: Open config file (schedule file)")
    print("2: New config file (schedule file)")
    print("3: Exit")
    inputData = int(input("Enter your choice: "))
    
    if inputData == 1:
        clearTerminal()
        openConfigFile()
    elif inputData == 2:
        clearTerminal()
        newConfigFile()
    elif inputData == 3:
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