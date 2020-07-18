-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- Task 17 - list all genres not linked to the show Dexter.
SELECT name FROM tv_genres WHERE id NOT IN (SELECT c.id FROM tv_shows AS a LEFT JOIN tv_show_genres AS b ON a.id = b.show_id LEFT JOIN tv_genres AS c ON b.genre_id = c.id WHERE a.title = 'Dexter') ORDER BY name ASC;
