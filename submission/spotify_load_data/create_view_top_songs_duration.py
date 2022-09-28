
create_top_songs_duration_stmt = """
CREATE VIEW top_songs_duration (
    artist_name, 
    song_name, 
    duration_ms
) AS

SELECT artist_name, song_name, duration_ms
FROM artists ar
JOIN albums al ON ar.artist_id = al.artist_id
JOIN tracks tr ON al.album_id = tr.album_id
ORDER BY duration_ms DESC, artist_name ASC
LIMIT 10;
"""