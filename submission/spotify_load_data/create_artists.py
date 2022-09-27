table_name = 'artists'

create_stmt = """
CREATE TABLE IF NOT EXISTS {0} (
	artist_id			varchar(50)     NOT NULL,
	artist_name		    varchar(255),
	external_url		varchar(100),
	genre				varchar(100),
	image_url			varchar(100),
	followers			int,
	popularity 		    int,
	type				varchar(50),
	artist_uri			varchar(100)    NOT NULL
	);
""".format(table_name)
