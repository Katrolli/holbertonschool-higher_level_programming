#!/usr/bin/python3
'''Script that lists all states'''
import sys
import MySQLdb


if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=u, password=p, database=d)
    cr = db.cursor()
    cr.execute("SELECT * from states")
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    db.close()
