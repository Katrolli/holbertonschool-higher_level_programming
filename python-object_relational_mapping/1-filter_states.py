#!/usr/bin/python3
'''Module that lists all states starting with N'''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], charset='utf8')
    cr = db.cursor()
    cr.execute("SELECT * from states")
    states = cr.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
