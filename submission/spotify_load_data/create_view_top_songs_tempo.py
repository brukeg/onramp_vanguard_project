
create_view_stmt = """
CREATE VIEW top_songs_tempo (
    artist_name, 
    song_name, 
    tempo
) AS

SELECT artist_name, song_name, tempo
FROM artists ar
JOIN albums al USING (artist_id)
JOIN tracks tr USING (album_id)
JOIN track_features USING (track_id)
ORDER BY tempo DESC, artist_name ASC
LIMIT 10;
"""