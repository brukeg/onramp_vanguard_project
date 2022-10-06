
create_top_songs_tempo_stmt = """
CREATE VIEW IF NOT EXISTS top_songs_tempo (
    artist_name, 
    song_name, 
    tempo
) AS

SELECT artist_name, song_name, tempo
FROM (
    SELECT 
        ar.artist_name
        , tr.song_name
        , tf.tempo
        , ROW_NUMBER() OVER (
            PARTITION BY ar.artist_name 
            ORDER BY tf.tempo DESC
        ) AS row_num
    FROM artist ar
    JOIN album al USING (artist_id)
    JOIN track tr USING (album_id)
    JOIN track_feature tf USING (track_id)
)
WHERE row_num < 11
ORDER BY artist_name ASC, tempo DESC;
"""