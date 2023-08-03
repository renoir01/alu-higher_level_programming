-- the database dump from hbtn_0d_tvshows to your MySQL server
-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tvs.title, tvg.name
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg
ON tvsg.show_id = tvs.id
LEFT JOIN tv_genres AS tvg
ON tvg.id = tvsg.genre_id
ORDER BY tvs.title, tvg.name;
