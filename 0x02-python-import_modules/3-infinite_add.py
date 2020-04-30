#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    total = 0
    if args == 1:
        print("{}".format(0))
    else:
        for index in range(1, args):
            total += int(argv[index])
        print("{}".format(total))
