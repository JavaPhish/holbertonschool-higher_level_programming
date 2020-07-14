-- TV show dumpy
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres WHERE tv_show_genres.genre_id >= 1
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
