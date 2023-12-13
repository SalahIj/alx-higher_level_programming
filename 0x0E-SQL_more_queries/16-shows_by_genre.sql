-- Listing all shows..
SELECT title, t.name FROM tv_shows
LEFT JOIN tv_show_genres AS tg ON id=tg.show_id
LEFT JOIN tv_genres AS t ON tg.genre_id = t.id
ORDER BY title, t.name;
