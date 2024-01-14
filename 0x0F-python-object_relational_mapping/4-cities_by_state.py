#!/usr/bin/python3
""" The necessery modules imported """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    datab = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])

    cursor = datab.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")

    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    datab.close()
