#!/usr/bin/python3
"Script that computes data"
import sys


tot = 0
count = 0
code_list = []
for i, line in enumerate(sys.stdin):
    ls = line.split()
    size = int(ls[len(ls) - 1])
    s_code = ls[len(ls) - 2]
    tot += size
    code_list.append(s_code)
    code_list.sort()
    if count == 10:
        print("Filesize: {}".format(tot))
        count = 0
    elif count != 10:
        print("{}: {}".format(code_list[count], i))
        count += 1
