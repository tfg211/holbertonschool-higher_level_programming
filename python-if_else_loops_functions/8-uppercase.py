#!/usr/bin/python3
def uppercase(str):
    str_dest = ""
    for i in range(0, len(str)):
        if 'a' <= str[i] <= 'z':
            str_dest = str_dest + chr(ord(str[i]) - 32)
        else:
            str_dest = str_dest + str[i]
    print("{}".format(str_dest))
