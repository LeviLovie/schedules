import os
import json

import src.foo as foo

schedule = []
path = ""
newSchedule = ""

def openConfigFile(showListOfSchedules):
    global schedule
    global path

    if showListOfSchedules == False:
        print("Files:")
        files = os.listdir("schedules")
        for i in files:
            if i == files[-1]:
                print("'" + i + "'")
            else:
                print("'" + i + "'", end=", ")
        print()
        path = "schedules/" + input("Enter name of schedule file (without `.json`): ") + ".json"
    else:
        path = "schedules/" + newSchedule + ".json"
    
    try:
        with open(path) as json_file:
            schedule_json = json.load(json_file)
            schedule = [foo.User(u) for u in schedule_json]
    except FileNotFoundError:
        print("File not found")
        return

def newConfigFile(isDev):
    name = input("Enter name of schedule file (without `.json`): ")
    newSchedule = name
    name = "schedules/" + name + ".json"

    with open(name, 'w') as outfile:
        json.dump([], outfile)

    foo.clearTerminal(isDev)