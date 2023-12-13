-- Using 'hbtn_0d_tvshows' for listing...
SELECT tv_genres.name
FROM tv_genres AS tg
INNER JOIN tv_show_genres m ON tg.id = m.genre_id
INNER JOIN tv_shows s ON m.show_id = s.id
WHERE s.title = 'Dexter' ORDER BY tg.name ASC;
