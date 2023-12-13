-- Listing all shows without the genre.
SELECT tg.title FROM tv_shows AS tg
WHERE tg.id NOT IN (
	      SELECT tg.id FROM tv_shows AS tg
	      JOIN tv_show_genres AS ts ON tg.id=ts.show_id
	      JOIN tv_genres ON tv_genres.id=ts.genre_id
	      WHERE tv_genres.name = "Comedy" )
ORDER BY tg.title;
