-- This script lists all the cities of California that can be found in the database.
-- Task 8 - Cities of a states.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
