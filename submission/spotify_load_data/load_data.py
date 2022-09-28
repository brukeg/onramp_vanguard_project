import sqlite3
# from submission.spotify_ingest_data.get_data import artists_df, albums_df, tracks_df, track_features_df
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

# my_dict = {
#     'artists': artists_df,
#     'albums': albums_df,
#     'tracks': tracks_df,
#     'track_features': track_features_df,
# }

def create_tables(stmts: list, db_name: str):
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        for create_stmt in stmts:
            cur.execute(create_stmt)
            conn.commit()
    conn.close()


def insert_data(df: object, table_name: str, db_name):
    # print(df.head(1))
    # print(f"\n{table_name=}")
    with sqlite3.connect(db_name) as conn:
        cur=conn.cursor()
        df.to_sql(table_name, conn, if_exists='replace')
        cur.execute(f'SELECT * FROM {table_name};')
        conn.commit()
        result = cur.fetchall()
        print(result)
    conn.close()


def load_dfs(df_tuples: list, db_name):
    for df_info in df_tuples:
        df, table_name = df_info
        insert_data(df, table_name, db_name)
