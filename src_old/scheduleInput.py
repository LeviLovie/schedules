import json

import src.foo as foo
import src.config as config

def printVariations():
    print()
    print("1: Add user")
    print("2: Remove user")
    print("3: Change user")
    print("4: Save")
    print("5: Exit to menu")
    print("6: Full exit")
    print()

    try:
        chose = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input")
        return 0
    return chose

def chose_1(isDev):
    foo.clearTerminal(isDev)

    print("Users:")
    for i in config.schedule:
        if i == config.schedule[-1]:
            print("'" + i.nick + "'")
        else:
            print("'" + i.nick + "'", end=", ")

    name = input("Type name of user: ")
    timeZone = int(input("Type time zone of user (UTC+): "))
    minTime = int(input("Type min time of user: "))
    maxTime = int(input("Type max time of user: "))
    config.schedule.append(foo.User({
        "nick": name,
        "timeZone": timeZone,
        "minTime": minTime,
        "maxTime": maxTime
    }))

def chose_2(isDev):
    foo.clearTerminal(isDev)

    print("Users:")
    for i in config.schedule:
        if i == config.schedule[-1]:
            print("'" + i.nick + "'")
        else:
            print("'" + i.nick + "'", end=", ")

    name = input("Type name of user: ")
    for i in config.schedule:
        if i.nick == name:
            config.schedule.remove(i)
            break

def chose_3(isDev):
    foo.clearTerminal(isDev)

    print("Users:")
    for i in config.schedule:
        if i == config.schedule[-1]:
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
        for i in config.schedule:
            if i.nick == name:
                i.nick = newName
                break
    elif inputData == 2:
        newTimeZone = int(input("Type new time zone of user (UTC+): "))
        for i in config.schedule:
            if i.nick == name:
                i.timeZone = newTimeZone
                break
    elif inputData == 3:
        newMinTime = int(input("Type new min time of user: "))
        for i in config.schedule:
            if i.nick == name:
                i.minTime = newMinTime
                break
    elif inputData == 4:
        newMaxTime = int(input("Type new max time of user: "))
        for i in config.schedule:
            if i.nick == name:
                i.maxTime = newMaxTime
                break
    elif inputData == 5:
        newName = input("Type new name of user: ")
        newTimeZone = int(input("Type new time zone of user (UTC+): "))
        newMinTime = int(input("Type new min time of user: "))
        newMaxTime = int(input("Type new max time of user: "))
        for i in config.schedule:
            if i.nick == name:
                i.nick = newName
                i.timeZone = newTimeZone
                i.minTime = newMinTime
                i.maxTime = newMaxTime
                break
    elif inputData == 6:
        foo.clearTerminal(isDev)
        return

def chose_4(isDev):
    foo.clearTerminal(isDev)

    with open(config.path, 'w') as outfile:
        json.dump([u.__dict__ for u in config.schedule], outfile)

def general(isDev):
    chose = printVariations()
    if chose == 1:
        chose_1(isDev)
        return 0
    elif chose == 2:
        chose_2(isDev)
        return 0
    elif chose == 3:
        chose_3(isDev)
        return 0
    elif chose == 4:
        chose_4(isDev)
        return 0
    elif chose == 5:
        foo.clearTerminal(isDev)
        return 1
    elif chose == 6:
        foo.clearTerminal(isDev)
        exit(0)
    else:
        foo.clearTerminal(isDev)
        print("Invalid input")
        return 0