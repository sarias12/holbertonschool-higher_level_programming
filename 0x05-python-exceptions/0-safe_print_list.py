#!/usr/bin/pyhton3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for element in my_list[:x]:
            count += 1
            print("{}".format(element), end="")
        print()
        return count
    except:
        print("An unexpected error has occurred")
