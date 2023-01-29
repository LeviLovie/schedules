import sys

import src_old.helping as helping
import src_old.printTime as printTime
import src_old.config as config
import src_old.scheduleInput as scheduleInput
from src_old import db

isDev = False

def workOnSchedule():
    helping.clearTerminal(isDev)
    print("\033[1;33mSchedule:\033[0m")

    printTime.printNameTableLine()
    printTime.table()
    printTime.UTC_body()

    # printTime.printNameTableLine()
    # printTime.table()
    # printTime.LOC_body(0)

    printTime.upperLine()

    for i in db.get_users(db.open_db()):
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
        # config.openConfigFile(False)
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
    
    db.add_user(db.open_db(), helping.User("Vlad", -4, -5, 5))
    db.add_user(db.open_db(), helping.User("Leo", 7, -7, 3))

    helping.clearTerminal(isDev)
    print("\033[1;33mYour size of terminal have to be biger, tht 175:25\033[0m")
    main()