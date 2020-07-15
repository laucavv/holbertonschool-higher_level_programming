-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy
SELECT tv_shows.title FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = "comedy" ORDER BY tv_shows.title ASC;

