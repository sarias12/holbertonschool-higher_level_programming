def uppercase(str):
    for char in str:
        char = ord(char)
        if char >= 97 and char <= 122:
            char -= 32
        print("{}".format(chr(char)), end="")
    print()
