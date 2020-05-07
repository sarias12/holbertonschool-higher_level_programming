def print_sorted_dictionary(a_dictionary):
    sort_dictionary = sorted(a_dictionary.items())
    for key, value in sort_dictionary:
        print("{}: {}".format(key, value))
