-- This script creates the table unique_id on your MySQL server.
-- Task 5 - creates table with mandatory id and must be unique.
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
