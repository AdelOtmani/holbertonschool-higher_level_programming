-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_shows.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_shows.genres_id
GROUP BY genre
ORDER BY tv_shows.title, tv_show_genres.genre_id;
