
create_top_songs_tempo_stmt = """
CREATE VIEW IF NOT EXISTS top_songs_tempo (
    artist_name, 
    song_name, 
    tempo
) AS

SELECT artist_name, song_name, tempo
FROM artist ar
JOIN album al USING (artist_id)
JOIN track tr USING (album_id)
JOIN track_feature USING (track_id)
ORDER BY tempo DESC, artist_name ASC
LIMIT 10;
"""