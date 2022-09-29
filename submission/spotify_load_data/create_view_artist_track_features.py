
create_artist_track_feat_stmt = """
CREATE VIEW IF NOT EXISTS artist_track_features (
    artist_name,
    genre,
    artist_popularity,
    artist_followers,
    song_name,
    track_duration_ms,
    explicit,
    track_type,
    danceability,
    energy,
    instrumentalness,
    liveness,
    loudness,
    speechiness,
    tempo,
    valence,
    track_feature_type,
    release_date,
    album_name,
    album_type
) AS

WITH artists_albums AS (
    SELECT
        ar.artist_name
        , ar.genre
        , ar.popularity AS artist_popularity
        , ar.followers AS artist_followers
        , al.release_date
        , al.album_name
        , al.type AS album_type
        , al.album_id
    FROM artist ar
    JOIN album al USING (artist_id)
),

album_tracks AS (
    SELECT
        aa.*
        , tr.song_name
        , tr.duration_ms AS track_duration_ms
        , tr.explicit
        , tr.type AS track_type
        , tr.track_id
    FROM artists_albums aa
    JOIN track tr USING(album_id)
),

tracks_track_features AS (
    SELECT
        at.*
        , tf.danceability
        , tf.energy
        , tf.instrumentalness
        , tf.liveness
        , tf.loudness
        , tf.speechiness
        , tf.tempo
        , tf.type AS track_feature_type
        , tf.valence
    FROM album_tracks at
    JOIN track_feature tf USING (track_id)
)

SELECT
    artist_name
    , genre
    , artist_popularity
    , artist_followers
    , song_name
    , track_duration_ms
    , explicit
    , track_type
    , danceability
    , energy
    , instrumentalness
    , liveness
    , loudness
    , speechiness
    , tempo
    , valence
    , track_feature_type
    , release_date
    , album_name
    , album_type
FROM tracks_track_features
ORDER BY artist_name ASC, release_date ASC;
"""