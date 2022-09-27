table_name = 'albums'

create_stmt = """
CREATE TABLE IF NOT EXISTS {0} (
	album_id			varchar(50)     NOT NULL,
	album_name			varchar(255),
	external_url		varchar(100),
	image_url			varchar(100),
	release_date		date,
	total_tracks		int,
	type				varchar(50),
	album_uri			varchar(100)    NOT NULL,
	artist_id			varchar(50)     NOT NULL
	);
""".format(table_name)