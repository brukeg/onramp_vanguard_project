

create_top_artists_stmt = """
CREATE VIEW IF NOT EXISTS top_artists (
    artist_name, 
    followers
) AS

SELECT artist_name, followers
FROM artist 
ORDER BY popularity DESC
LIMIT 20;
"""