-- prints all cities
SELECT cities.id, cities.name, states.name FROM states, cities
ORDER BY cities.id ASC;
