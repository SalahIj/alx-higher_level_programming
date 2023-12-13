-- Listing all shows in Database 'hbtn_0d_tvshows'.
SELECT t.title, tg.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS tg ON tg.show_id = t.id
WHERE tg.show_id IS NULL
ORDER BY t.title ASC, tg.genre_id ASC;
