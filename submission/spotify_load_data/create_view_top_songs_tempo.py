
create_top_songs_tempo_stmt = """
CREATE VIEW IF NOT EXISTS top_songs_tempo (
    artist_name, 
    song_name, 
    tempo
) AS

SELECT ar.artist_name, tr.song_name, tf.tempo
FROM artist ar
JOIN album al USING (artist_id)
JOIN track tr USING (album_id)
JOIN track_feature tf USING (track_id)
ORDER BY ar.artist_name ASC, tf.tempo DESC
LIMIT 10;
"""