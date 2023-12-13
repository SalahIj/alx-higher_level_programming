-- Listing all genres.
SELECT name FROM tv_genres AS tg
WHERE tg.id NOT IN (
	      SELECT tg.id FROM tg
	      JOIN tv_show_genres AS ts ON tg.id=ts.genre_id
	      JOIN tv_shows AS ta ON ta.id=ts.show_id
	      WHERE ta.title = "DEXTER" )
ORDER BY tg.name;
