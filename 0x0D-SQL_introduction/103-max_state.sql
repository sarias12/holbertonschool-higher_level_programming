-- This script displays the max temperature of each state (ordered by State name).
-- Task 103 - MAX Temperatures
SELECT state, MAX(value) FROM temperatures GROUP BY state;
