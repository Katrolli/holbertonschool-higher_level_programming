#!/usr/bin/python3
'''Module that lists state searched by argv[4]'''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], charset='utf8')
    cr = db.cursor()
    query = " ".join([
        "SELECT cities.name",
        "FROM cities JOIN states ON states.id = cities.state_id",
        "WHERE states.name LIKE %s"
        ])
    cr.execute(query, (sys.argv[4], ))
    cities = cr.fetchall()
    for i in range(len(cities)):
        if i == len(cities) - 1:
            print("{}".format(cities[i][0]), end='')
        else:
            print("{}, ".format(cities[i][0]), end='')
    print()
    cr.close()
    db.close()
