-- Listing all shows in Database 'hbtn_0d_tvshows'.
SELECT t.title, tv_show_genres.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = t.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY t.title ASC, tv_show_genres.genre_id ASC;
