#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i and i + j != 17:
            print("{}{}".format(i, j), end=", ")
        elif i + j == 17 and i < 9:
            print("{}{}".format(i, j), end="\n")
