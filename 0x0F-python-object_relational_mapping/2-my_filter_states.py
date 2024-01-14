#!/usr/bin/python3
""" Importe necessery Modules """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    datab = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])

    cursor = datab.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(query)

    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    datab.close()
