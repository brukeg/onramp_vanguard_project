
create_avg_loudness_stmt = """
CREATE VIEW IF NOT EXISTS avg_loudness (
    genre,
    release_date,
    avg_loudness
) AS

SELECT genre, release_date, avg_loudness
FROM (
    SELECT
        genre
        , album_name
        , release_date
        , ROUND(
            AVG(loudness) OVER (
                PARTITION BY album_name
                )
            , 2) AS avg_loudness
FROM artist_track_features
    )
GROUP BY genre, release_date, avg_loudness
ORDER BY genre ASC, release_date ASC;
"""