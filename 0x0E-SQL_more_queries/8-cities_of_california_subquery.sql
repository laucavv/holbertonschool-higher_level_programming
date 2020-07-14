-- Script that lists all the cities of California that can be found in the database
-- The states table contains only one record where name = California.
SELECT id, name FROM cities WHERE state_id = 1 ORDER BY id ASC;
