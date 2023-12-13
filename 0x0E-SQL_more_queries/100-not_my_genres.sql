sting all genres.
SELECT name FROM tv_genres AS
WHERE tv_genres.id NOT IN (
	      SELECT tv_genres.id FROM tv_genres
	      JOIN tv_show_genres AS tg ON tv_genres.id=tg.genre_id
	      JOIN tv_shows ON tv_shows.id=tg.show_id
	      WHERE tv_shows.title = "DEXTER" )
ORDER BY tv_genres.name;
