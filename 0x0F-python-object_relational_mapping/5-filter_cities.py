#!/usr/bin/python3
""" The necessery imported modules """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    datab = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])

    cursor = datab.cursor()
    cursor.execute("SELECT cities.id, cities.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   WHERE states.name = %s", [argv[4]])

    rows = cursor.fetchall()
    k = []
    for i in rows:
        k.append(i[1])
    print(", ".join(k))

    cursor.close()
    datab.close()
