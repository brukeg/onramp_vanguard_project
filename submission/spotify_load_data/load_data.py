import sqlite3
from submission.spotify_load_data.create_table_artists import create_artists_stmt
from submission.spotify_load_data.create_table_albums import create_albums_stmt
from submission.spotify_load_data.create_table_tracks import create_tracks_stmt
from submission.spotify_load_data.create_table_track_features import create_track_features_stmt
from submission.spotify_load_data.create_view_top_songs_duration import create_top_songs_duration_stmt
from submission.spotify_load_data.create_view_top_artists import create_top_artists_stmt
from submission.spotify_load_data.create_view_top_songs_tempo import create_top_songs_tempo_stmt


create_table_stmts = [
    create_artists_stmt,
    create_albums_stmt,
    create_tracks_stmt,
    create_track_features_stmt
]

create_view_stmts =[
    create_top_songs_duration_stmt,
    create_top_artists_stmt,
    create_top_songs_tempo_stmt
]


def create_tables(stmts: list, db_name: str):
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        for create_stmt in stmts:
            cur.execute(create_stmt)
            conn.commit()
    conn.close()


def insert_table_data(dataframe: object, table_name: str, db_name: str):
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        dataframe.to_sql(table_name, conn, if_exists='replace')
        cur.execute(f'SELECT * FROM {table_name};')
        conn.commit()
        result = cur.fetchall()
        print(result)
    conn.close()


def load_dfs(df_tuples: list, db_name: str):
    for df_info in df_tuples:
        df, table_name = df_info
        insert_table_data(df, table_name, db_name)

def create_views(stmts: list, db_name: str):
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        for create_stmt in stmts:
            cur.execute(create_stmt)
            conn.commit()
    conn.close()