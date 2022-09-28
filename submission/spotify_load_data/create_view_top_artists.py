

create_top_artists_stmt = """
CREATE VIEW top_artists (
    artist_name, 
    popularity
) AS

SELECT artist_name, popularity
FROM artists 
ORDER BY popularity DESC
LIMIT 20;
"""