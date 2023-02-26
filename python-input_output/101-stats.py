#!/usr/bin/python3
'''Module that computes data'''
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
i = 0
j = 0
try:
    while True:
        i = 0
        for line in sys.stdin:
            ls = line.split()
            size = int(ls[len(ls) - 1])
            s_code = ls[len(ls) - 2]
            tot += size
            code_list.append(s_code)
            code_list.sort()
            if s_code in code_d:
                code_d[s_code] += 1
            i += 1
            if i == 10:
                break
        print("Filesize: {}".format(tot))
        for key, value in code_d.items():
            if value != 0:
                print(f"{key}: {value}")
except KeyboardInterrupt:
    for line in sys.stdin:
        ls = line.split()
        size = int(ls[len(ls) - 1])
        s_code = ls[len(ls) - 2]
        tot += size
        code_list.append(s_code)
        code_list.sort()
    print("Filesize: {}".format(tot))
    for key, value in code_d.items():
        if value != 0:
            print(f"{key}: {value}")
