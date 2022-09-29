

create_top_artists_stmt = """
CREATE VIEW IF NOT EXISTS top_artists (
    artist_name, 
    followers
) AS

SELECT ar.artist_name, ar.followers
FROM artist ar
ORDER BY ar.followers DESC
LIMIT 20;
"""