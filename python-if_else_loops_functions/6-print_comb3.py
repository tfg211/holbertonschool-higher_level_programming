#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if (a != 0 or b != 1) and b > a:
            print(", ", end="")
        if b > a:
            print("{}{}".format(a, b), end="")
print("")
