#!/usr/bin/pyhton3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list[:x]:
            count += 1
            print("{}".format(element), end="")
        print("")
    except IndexError:
        print("")
    return count
