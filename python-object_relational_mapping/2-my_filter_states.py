#!/usr/bin/python3
'''Module that lists state searched by argv[4]'''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], charset='utf8')
    cr = db.cursor()
    cr.execute("SELECT * from states WHERE states.name LIKE BINARY '{}'"
               .format(sys.argv[4]))
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    db.close()
