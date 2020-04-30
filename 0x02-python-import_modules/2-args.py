#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    if args == 1:
        print("{} arguments.".format(0))
    elif args == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(args))
        for index in range(1, args):
            print("{}: {}".format(index, argv[index]))
