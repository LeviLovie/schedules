import sys

import src.helping as helping
import src.printTime as printTime
import src.config as config
import src.scheduleInput as scheduleInput

isDev = False

def workOnSchedule():
    global schedule
    helping.clearTerminal(isDev)
    print("\033[1;33mSchedule:\033[0m")

    printTime.printNameTableLine()
    printTime.table()
    printTime.UTC_body()

    # printTime.printNameTableLine()
    # printTime.table()
    # printTime.LOC_body(0)

    printTime.upperLine()

    for i in config.schedule:
        print("|", end="")
        print("\033[1;32m" + i.nick.center(20) + "\033[1;0m", end="")
        print("|", end="")
        printTime.general(i)
        print("|")
    
    printTime.lowerLine()

    result = scheduleInput.general(isDev)
    if result == 0:
        workOnSchedule()
    elif result == 1:
        main()

def main():
    print("1: Open config file (schedule file)")
    print("2: New config file (schedule file)")
    print("3: Exit")
    print()
    inputData = int(input("Enter your choice: "))
    
    if inputData == 1:
        helping.clearTerminal(isDev)
        config.openConfigFile(False)
        workOnSchedule()
    elif inputData == 2:
        helping.clearTerminal(isDev)
        config.newConfigFile(isDev)
        config.openConfigFile(False)
    elif inputData == 3:
        helping.clearTerminal(isDev)
        exit(0)
    else:
        helping.clearTerminal(isDev)
        print("Invalid input")
        return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--dev":
            isDev = True

    helping.clearTerminal(isDev)
    print("\033[1;33mYour size of terminal have to be biger, tht 175:25\033[0m")
    main()