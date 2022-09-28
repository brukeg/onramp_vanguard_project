
create_track_features_stmt = """
CREATE TABLE IF NOT EXISTS track_features (
	track_id			varchar(50) NOT NULL,
	danceability		double,
	energy				double,
	instrumentalness	double,
	liveness			double,
	loudness			double,
	speechiness			double,
	tempo				double,
	type				varchar(50),
	valence				double,
	song_uri			varchar(100) NOT NULL,
	CONSTRAINT song_uri_pk PRIMARY KEY (song_uri)
	);
"""