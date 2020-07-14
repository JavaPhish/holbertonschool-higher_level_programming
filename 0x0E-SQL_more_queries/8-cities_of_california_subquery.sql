-- stuff from cali
SELECT cities.id, cities.name FROM cities, states
WHERE state_id = 1
ORDER BY cities.id ASC;
