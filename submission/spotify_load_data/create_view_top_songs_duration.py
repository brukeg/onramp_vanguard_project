
create_top_songs_duration_stmt = """
CREATE VIEW IF NOT EXISTS top_songs_duration (
    artist_name, 
    song_name, 
    duration_ms
) AS

SELECT artist_name, song_name, duration_ms
FROM (
    SELECT 
        ar.artist_name
        , tr.song_name
        , tr.duration_ms
        , ROW_NUMBER() OVER (
            PARTITION BY ar.artist_name 
            ORDER BY tr.duration_ms DESC
        ) AS row_num
    FROM artist ar
    JOIN album al USING (artist_id)
    JOIN track tr USING (album_id)
)
WHERE row_num < 11
ORDER BY artist_name ASC, duration_ms DESC;
"""