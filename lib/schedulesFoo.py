from . import db
from . import foo


firstTimeSymols   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
secondTimeSymbols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]


def add_user(isDev, scheduleName):
    foo.clearTerminal(isDev)
    print(foo.COLOR_CYAN + "Add User" + foo.COLOR_RESET)
    print()
    useerName = input("Enter user name: ")
    db.add_userToShedule(db.open_db(), useerName, scheduleName)
    return 0


def delete_user(isDev, scheduleName):
    foo.clearTerminal(isDev)
    print(foo.COLOR_CYAN + "Delete User" + foo.COLOR_RESET)
    print()
    userName = input("Enter user name: ")
    db.delete_userToSchedule(db.open_db(), userName, scheduleName)
    return 0


def printBottom():
    print("+" + ("-" * 20) + "+" + ("-" * ((24 * 2) + 1)) + "+")

def printHeader():
    print("+" + ("-" * 20) + "+" + ("-" * ((24 * 2) + 1)) + "+")
    
    print("|" + foo.COLOR_GREEN + ("*0".center(20)) + foo.COLOR_RESET + "|", end="")
    for i in range(2):
        print(foo.COLOR_CYAN + "@" + foo.COLOR_RESET, end="")
        for j in range(len(firstTimeSymols)):
            print(foo.COLOR_GREEN + str(firstTimeSymols[j]) + foo.COLOR_RESET, end="")
    print(foo.COLOR_CYAN + "@" + foo.COLOR_RESET + "|")

    print("|" + foo.COLOR_GREEN + ("0*".center(20)) + foo.COLOR_RESET + "|", end="")
    for i in range(2):
        print(foo.COLOR_CYAN + "@" + foo.COLOR_RESET, end="")
        for j in range(len(secondTimeSymbols)):
            print(foo.COLOR_GREEN + str(secondTimeSymbols[j]) + foo.COLOR_RESET, end="")
    print(foo.COLOR_CYAN + "@" + foo.COLOR_RESET + "|")

    print("+" + ("-" * 20) + "+" + ("-" * ((24 * 2) + 1)) + "+")


def print_schedules(schedules):
    i = 0
    for schedule in schedules:
        if i % 5 == 0:
            print()
        print((schedule["name"]).ljust(10), end=" ")
        i += 1
    print()


def add_schedule(isDev):
    foo.clearTerminal(isDev)
    print(foo.COLOR_CYAN + "Add Schedule" + foo.COLOR_RESET)
    print()
    name = input("Enter schedule name: ")
    db.add_schedule(db.open_db(), name)
    return 0

def delete_schedule(isDev):
    foo.clearTerminal(isDev)
    print(foo.COLOR_CYAN + "Delete Schedule" + foo.COLOR_RESET)
    print()
    name = input("Enter schedule name: ")
    db.delete_schedule(db.open_db(), name)
    return 0