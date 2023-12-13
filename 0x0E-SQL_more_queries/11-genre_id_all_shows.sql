-- Listing all shows in databases 'hbtn_0d_tvshows'
SELECT tv_shows.title, s.genre_id
FROM tv_show_genres AS s
RIGHT JOIN tv_shows ON s.show_id = tv_shows.id
ORDER BY tv_shows.title, s.genre_id;
