table_name = 'albums'

create_stmt = """
CREATE TABLE IF NOT EXISTS {0} (
	track_id			varchar(50) 	NOT NULL,
	song_name			varchar(255),
	external_url		varchar(100),
	duration_ms			int,
	explicit			boolean,
	disc_number			int,
	type				varchar(50),
	song_uri			varchar(100)	NOT NULL,
	album_id			varchar(50)		NOT NULL
	);
""".format(table_name)