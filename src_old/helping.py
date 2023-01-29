import os

def clearTerminal(isDev):
    print("\033c", end="")
    if isDev: print("\033[1;33mRunning in dev mode\033[0m")

def GetListOfSchedules():
    print("Files:")
    files = os.listdir("schedules")
    for i in files:
        if i == files[-1]:
            print("'" + i + "'")
        else:
            print("'" + i + "'", end=", ")
    print()

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

firstTimeSymols   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
secondTimeSymbols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]