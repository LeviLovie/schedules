import src.foo as foo

def printNameTableLine():
    print("+", end="")
    for i in range(20):
        print("-", end="")
    print("+", end="")
    for i in range((24 * 3) + 1):
        print("-", end="")
    print("+")

def table():
    print("|", end="")
    print("\033[1;32m" + "UTC+0".center(20) + "\033[1;0m", end="")
    print("|", end="")
    for i in range(3):
        print("\033[1;36m@\033[1;32m", end="")
        for i in range(len(foo.firstTimeSymols)):
            print(str(foo.firstTimeSymols[i]), end="")
    print("\033[1;36m@\033[1;0m|")

def UTC_body():
    print("|", end="")
    print("".center(20), end="")
    print("|", end="")
    for i in range(3):
        print("\033[1;36m@\033[1;32m", end="")
        for i in range(len(foo.secondTimeSymbols)):
            print(str(foo.secondTimeSymbols[i]), end="")
    print("\033[1;36m@\033[1;0m|")



def LOC_body(localTime):
    print("|", end="")
    print("".center(20), end="")
    print("|", end="")
    # for i in range(3):
    for j in range(len(foo.secondTimeSymbols)):
        if j + localTime == 0 or j + localTime == 24:
            print("\033[1;36m@\033[1;0m", end="")
        if j + localTime > 0 and j + localTime < 24:
            print("\033[1;32m" + str(foo.secondTimeSymbols[j]) + "\033[1;0m", end="")
        # if i + localTime == 0 or i + localTime == 24 or i + localTime == 48:
        #     print("\033[1;36m@\033[1;32m1\033[1;0m", end="")
        # elif i + localTime < 24 or i + localTime < 48 or i + localTime < 72:
        #     print("\033[1;32m" + str(secondTimeSymbols[i + localTime]) + "\033[1;0m", end="")
        # else:
        #     print("\033[1;32m" + str(secondTimeSymbols[localTime]) + "\033[1;0m", end="")
    print()

def upperLine():
    print("+", end="")
    print(("-" * 20).center(20), end="")
    print("+", end="")
    for i in range((24 * 3) + 1):
        print("-", end="")
    print("+")

def lowerLine():
    print("+", end="")
    for i in range(20):
        print("-", end="")
    print("+", end="")
    for i in range((24 * 3) + 1):
        print("-", end="")
    print("+")

def general(i):
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