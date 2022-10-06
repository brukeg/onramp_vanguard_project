
create_top_songs_duration_stmt = """
CREATE VIEW IF NOT EXISTS top_songs_duration (
    artist_name, 
    song_name, 
    duration_ms
) AS

SELECT ar.artist_name, tr.song_name, tr.duration_ms
FROM artist ar
JOIN album al USING (artist_id)
JOIN track tr USING (album_id)
ORDER BY ar.artist_name ASC, tr.duration_ms DESC   
LIMIT 10;
"""