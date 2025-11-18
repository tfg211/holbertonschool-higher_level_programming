#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 0
    for i in sys.argv[1:]:
        a += int(i)
    print(a)
