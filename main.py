import sys

from lib import foo
from lib import users
from lib import schedules


isDev = False


def main():
    global isDev
    print(foo.COLOR_CYAN + "Main menu" + foo.COLOR_RESET)
    print("1. Users")
    print("2. Schedules")
    print("5. Exit")
    print()

    try:
        chose = int(input("Enter your choice: "))
    except ValueError:
        foo.clearTerminal(isDev)
        print(foo.COLOR_YELLOW + "Invalid input" + foo.COLOR_RESET)
        main()
    
    if chose == 1:
        foo.clearTerminal(isDev)
        result = users.general(isDev)
        if result == 0:
            foo.clearTerminal(isDev)
            main()
        else:
            foo.clearTerminal(isDev)
            print(foo.COLOR_YELLOW + "It's with unknow error, please, see, did you it correct" + foo.COLOR_RESET)
            main()
    elif chose == 2:
        foo.clearTerminal(isDev)
        result = schedules.general(isDev)
        if result == 0:
            foo.clearTerminal(isDev)
            main()
        else:
            foo.clearTerminal(isDev)
            print(foo.COLOR_YELLOW + "It's with unknow error, please, see, did you it correct" + foo.COLOR_RESET)
            main()
    elif chose == 5:
        foo.clearTerminal(isDev)
        exit(0)
    else:
        foo.clearTerminal(isDev)
        print(foo.COLOR_YELLOW + "Invalid input" + foo.COLOR_RESET)
        main()


if __name__ == "__main__":
    foo.clearTerminal(isDev)

    if len(sys.argv) > 1:
        if sys.argv[1] == "--dev":
            isDev = True

    main()