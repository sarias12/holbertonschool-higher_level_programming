-- This script creates the table id_not_null on your MySQL server.
-- Task 4 - creates table with mandatory id and default value 1.
CREATE TABLE IF NOT EXISTS id_not_null (id INT NOT NULL DEFAULT 1, name VARCHAR(256));
