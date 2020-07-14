-- This script  lists all cities contained in the database hbtn_0d_usa.
-- Task 10 - Listing cities by states.
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states WHERE cities.state_id = states.id;
