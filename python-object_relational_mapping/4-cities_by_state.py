#!/usr/bin/python3
'''Module that lists state searched by argv[4]'''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], charset='utf8')
    cr = db.cursor()
    cr.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state.id")
    cities = cr.fetchall()
    for city in cities:
        print(city)
    cr.close()
    db.close()
