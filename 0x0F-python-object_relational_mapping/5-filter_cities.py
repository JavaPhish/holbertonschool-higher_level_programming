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
    sql = "SELECT cities.name, states.name FROM cities, states"
    wheresql = "WHERE state_id=states.id"
    curs.execute("{} {} ORDER BY cities.id ASC".format(sql, wheresql))

    """ Save the data from the query """
    query = curs.fetchall()

    cities = []
    """ Store all individial cities in an array (Im lazy so) """
    for rows in query:
        if (rows[1] == sys.argv[4]):
            cities.append(rows[0])

    """ Print it to match checkers output """
    for cityn in range(0, len(cities)):
        if cityn == 0:
            print(cities[cityn], end="")
        else:
            print(", {}".format(cities[cityn]), end="")

    print("")

    """ Close the connections b4 we leave and get mcdonalds """
    """ I want mcdonalds. """
    curs.close()
    connection.close()
