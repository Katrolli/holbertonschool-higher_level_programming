-- Join tables to list cities by state
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id GROUP BY cities.id;
