from . import db
from . import foo

def general(isDev):
    foo.clearTerminal(isDev)
    print(foo.COLOR_CYAN + "Users" + foo.COLOR_RESET)
    users = db.get_users(db.open_db())
    print("+" + "-" * 5 + "+" + "-" * 20 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+")
    print("|" + "num".center(5) + "|" + "name".center(20) + "|" + "tz".center(5) + "|" + "min".center(5) + "|" + "max".center(5) + "|")
    print("+" + "-" * 5 + "+" + "-" * 20 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+")
    for i in users:
        print("|" + foo.COLOR_GREEN + str(users.index(i)).center(5) + foo.COLOR_RESET + "|" + foo.COLOR_GREEN + i.nick.center(20) + foo.COLOR_RESET + "|" + foo.COLOR_GREEN + str(i.timeZone).center(5) + foo.COLOR_RESET + "|" + foo.COLOR_GREEN + str(i.minTime).center(5) + foo.COLOR_RESET + "|" + foo.COLOR_GREEN + str(i.maxTime).center(5) + foo.COLOR_RESET + "|")
    print("+" + "-" * 5 + "+" + "-" * 20 + "+" + "-" * 5 + "+" + "-" * 5 + "+" + "-" * 5 + "+")
    print()
    
    print("1. Add User")
    print("2. Remove User")
    print("3. Change User")
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
        print(foo.COLOR_CYAN + "Add User" + foo.COLOR_RESET)

        try:
            nick = input("Enter nick: ")
        except ValueError:
            foo.clearTerminal(isDev)
            return 0
        try:
            timeZone = int(input("Enter time zone: "))
        except ValueError:
            foo.clearTerminal(isDev)
            return 0
        try:
            minTime = int(input("Enter min time: "))
        except ValueError:
            foo.clearTerminal(isDev)
            return 0
        try:
            maxTime = int(input("Enter max time: "))
        except ValueError:
            foo.clearTerminal(isDev)
            return 0
        
        db.add_user(db.open_db(), foo.User({"nick": nick, "timeZone": timeZone, "minTime": minTime, "maxTime": maxTime}))
        general(isDev)
    elif chose == 2:
        foo.clearTerminal(isDev)
        print(foo.COLOR_CYAN + "Remove User" + foo.COLOR_RESET)
        nick = input("Enter nick: ")
        db.delete_user(db.open_db(), nick)
        general(isDev)
    elif chose == 3:
        foo.clearTerminal(isDev)
        print(foo.COLOR_CYAN + "Change User" + foo.COLOR_RESET)
        nick = input("Enter nick: ")

        try:
            timeZone = int(input("Enter time zone: "))
        except ValueError:
            foo.clearTerminal(isDev)
            return 0
        try:
            minTime = int(input("Enter min time: "))
        except ValueError:
            foo.clearTerminal(isDev)
            return 0
        try:
            maxTime = int(input("Enter max time: "))
        except ValueError:
            foo.clearTerminal(isDev)
            return 0
        
        db.set_user(db.open_db(), foo.User({"nick": nick, "timeZone": timeZone, "minTime": minTime, "maxTime": maxTime}))
        general(isDev)
    elif chose == 5:
        foo.clearTerminal(isDev)
        return 0
    else:
        foo.clearTerminal(isDev)
        return 1