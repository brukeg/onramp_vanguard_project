
create_top_songs_duration_stmt = """
CREATE VIEW IF NOT EXISTS top_songs_duration (
    artist_name, 
    song_name, 
    duration_ms
) AS

SELECT artist_name, song_name, duration_ms
FROM artist ar
JOIN album al ON ar.artist_id = al.artist_id
JOIN track tr ON al.album_id = tr.album_id
ORDER BY duration_ms DESC, artist_name ASC
LIMIT 10;
"""