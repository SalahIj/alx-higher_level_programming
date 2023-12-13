-- Listing all Comedy shows in db hbtn_0d_tvshows
SELECT title FROM tv_shows
JOIN tv_show_genres AS tg ON id=tg.show_id
JOIN tv_genres AS t ON t.id=tg.genre_id
WHERE t.name = 'Comedy'
ORDER BY title;
