-- Listing all shows from 'hbtn_0d_tvshows_rate'.
SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_shows AS ts
INNER JOIN tv_show_ratings AS tsr ON ts.id = tsr.show_id
GROUP BY tsr.show_id
ORDER BY rating DESC;
