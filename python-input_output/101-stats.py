#!/usr/bin/python3
"Script that computes data"
import sys


tot = 0
count = 0
code_list = []
code_d = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
for line in sys.stdin:
    ls = line.split()
    size = int(ls[len(ls) - 1])
    s_code = ls[len(ls) - 2]
    tot += size
    code_list.append(s_code)
    code_list.sort()
    if count == 10 or count == 0:
        print("Filesize: {}".format(tot))
        count += 1
    elif count in range(1, 10):
        if s_code in code_d:
            code_d[s_code] += 1
            print("{}: {}".format(code_list[count], code_d[s_code]))
            count += 1
            if count >= 10:
                count = 0
