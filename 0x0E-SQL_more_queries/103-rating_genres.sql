-- Listing all genres in 'hbtn_0d_tvshows_rate'...
SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
INNER JOIN tv_show_ratings AS tsr ON tsg.show_id = tsr.show_id
GROUP BY tsg.genre_id
ORDER BY rating DESC;
