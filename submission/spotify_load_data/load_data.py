import sqlite3
from submission.spotify_ingest_data.get_data import artists_df, albums_df, tracks_df, track_features_df
from submission.spotify_load_data.create_artists import create_artists_stmt
from submission.spotify_load_data.create_albums import create_albums_stmt
from submission.spotify_load_data.create_tracks import create_tracks_stmt
from submission.spotify_load_data.create_track_features import create_track_features_stmt


create_statement_list = [
    create_artists_stmt,
    create_albums_stmt,
    create_tracks_stmt,
    create_track_features_stmt
    ]

# dataframe_list = [artists_df, albums_df, tracks_df, track_features_df]
# table_name_list = ['artists', 'albums', 'tracks', 'track_features']

my_dict = {
    'artists': artists_df,
    'albums': albums_df,
    'tracks': tracks_df,
    'track_features': track_features_df,
}


def create_tables(stmts: list):
    with sqlite3.connect('spotify.db') as conn:
        cur = conn.cursor()
        for create_stmt in stmts:
            cur.execute(create_stmt)
            conn.commit()
    conn.close()

create_tables(create_statement_list)


def insert_artists():
    with sqlite3.connect('spotify.db') as conn:
        cur = conn.cursor()
        artists_df.to_sql('artist', conn, if_exists='replace')
        cur.execute(f'SELECT * FROM artists LIMIT 1;')
        result = cur.fetchone()[1]
        print(result)

    conn.close()

    return result

insert_artists()


def insert_albums():
    with sqlite3.connect('spotify.db') as conn:
        cur = conn.cursor()
        albums_df.to_sql('albums', conn, if_exists='replace')
        cur.execute(f'SELECT * FROM albums LIMIT 1;')
        result = cur.fetchone()[1]
        print(result)

    conn.close()

    return result

insert_albums()


def insert_tracks():
    with sqlite3.connect('spotify.db') as conn:
        cur = conn.cursor()
        tracks_df.to_sql('tracks', conn, if_exists='replace')
        cur.execute(f'SELECT * FROM tracks LIMIT 1;')
        result = cur.fetchone()[1]
        print(result)

    conn.close()

    return result

insert_tracks()


def insert_track_features():
    with sqlite3.connect('spotify.db') as conn:
        cur = conn.cursor()
        track_features_df.to_sql('track_features', conn, if_exists='replace')
        cur.execute(f'SELECT * FROM track_features LIMIT 1;')
        result = cur.fetchone()[1]
        print(result)

    conn.close()

    return result

insert_track_features()