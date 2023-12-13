-- Import data from...
SELECT g.title, g.genre_id
FROM tv_show_genres AS s
JOIN tv_shows as g 
ON s.show_id = g.id
ORDER BY g.title, s.genre_id;
