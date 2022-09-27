import sqlite3
from submission.spotify_ingest_data.get_data import artists_df, albums_df, tracks_df, track_features_df


def load_spotify_data(dataframe: object, stmt: str, table_name: str):
    with sqlite3.connect('spotify.db') as conn:
        c = conn.cursor()
        c.execute(stmt)
        conn.commit()

        dataframe.to_sql(table_name, conn, if_exists='replace')

        c.execute(f'SELECT * FROM {table_name}')

        for row in c.fetchall():
            print(row)
    conn.close()
