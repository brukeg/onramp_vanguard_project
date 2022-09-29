import sqlite3
from submission.spotify_load_data.create_table_artists import create_artists_stmt
from submission.spotify_load_data.create_table_albums import create_albums_stmt
from submission.spotify_load_data.create_table_tracks import create_tracks_stmt
from submission.spotify_load_data.create_table_track_features import create_track_features_stmt
from submission.spotify_load_data.create_view_top_songs_duration import create_top_songs_duration_stmt
from submission.spotify_load_data.create_view_top_artists import create_top_artists_stmt
from submission.spotify_load_data.create_view_top_songs_tempo import create_top_songs_tempo_stmt
from submission.spotify_load_data.create_view_artist_track_features import create_artist_track_feat_stmt
from submission.spotify_load_data.create_view_avg_loudness import create_avg_loudness_stmt

"""
Creates sql tables.
Inserts data into sql tables.
Creates sql views. 
"""

create_table_stmts = [
    create_artists_stmt,
    create_albums_stmt,
    create_tracks_stmt,
    create_track_features_stmt,
]

create_view_stmts = [
    create_top_songs_duration_stmt,
    create_top_artists_stmt,
    create_top_songs_tempo_stmt,
    create_artist_track_feat_stmt,
    create_avg_loudness_stmt,
]


def create_tables(stmts: list, db_name: str):
    """
    Creates tables in spotify.db based on definitions outlined in files prefixed with "create_table_"

    :param
        stmts (list): the sql statement to execute

    :param
        db_name (str): the file name of the database, spotify.db

    :return
        None:
    """
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        for create_stmt in stmts:
            cur.execute(create_stmt)
            conn.commit()
    conn.close()


def insert_table_data(dataframe: object, table_name: str, db_name: str):
    """
    Inserts data from a dataframe into a sql table.
    :param
        dataframe (object): the target dataframe to convert to a sql table

    :param
        table_name (object): the name of the table to insert records into

    :param
        db_name (object): the file name of the database, spotify.db

    :return
        None:
    """
    with sqlite3.connect(db_name) as conn:
        dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


def load_dfs(df_tuples: list, db_name: str):
    """
    Iterates through a tuple containing a dataframe and table name. Calls insert_table_data get dataframe into sql.

    :param
        df_tuples (list): tuple containing a dataframe and corresponding table name.

    :param
        db_name (list): the file name of the database, spotify.db

    :return
        None:
    """
    for df_info in df_tuples:
        df, table_name = df_info
        insert_table_data(df, table_name, db_name)


def create_views(stmts: list, db_name: str):
    """
    Creates sql views in spotify.db based on definitions outlined in files prefixed with "create_view_"

    :param
        stmts (list): the sql statement to execute

    :param
        db_name (str): the file name of the database, spotify.db

    :return
        None:
    """
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        for create_stmt in stmts:
            cur.execute(create_stmt)
            conn.commit()
    conn.close()
