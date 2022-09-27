table_name = 'track_features'

create_stmt = """
CREATE TABLE IF NOT EXISTS {0} (
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
	song_uri			varchar(100) NOT NULL
	);
""".format(table_name)