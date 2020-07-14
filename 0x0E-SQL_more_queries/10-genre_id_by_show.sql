-- TV show dumpy
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
