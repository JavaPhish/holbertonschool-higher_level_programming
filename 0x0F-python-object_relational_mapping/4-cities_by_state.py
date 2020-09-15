#!/usr/bin/python3
""" Basic MySQL (My squeel) query with an OEM """

import sys
import MySQLdb


if __name__ == "__main__":
    """ Arguments: mysql user, password, and DB name """

    """ Connect to already made SQL server with arguments """
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3], charset="utf8")

    """ Create a 'cursor' and execute a basic SQL query """
    curs = connection.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities, states"
    wheresql = "WHERE state_id=states.id"
    curs.execute("{} {} ORDER BY cities.id ASC".format(sql, wheresql))

    """ Save the data from the query """
    query = curs.fetchall()

    """ Print out the data from the query """
    for rows in query:
        print(rows)

    """ Close the connections b4 we leave and get mcdonalds """
    """ I want mcdonalds. """
    curs.close()
    connection.close()
