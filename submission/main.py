# import dataclasses
from submission.spotify_ingest_data.get_data import *
from submission.spotify_load_data.load_data import *
from submission.spotify_process_data.process_data import dedupe_data

"""
Establishes the file path to spotify.db.

Run __name__ == "__main__" to kick off the script.
"""
DB_NAME = "/Users/brukegetachew/Projects/onramp_vanguard_project/submission/spotify.db"

# what does this syntax do again?
def ingest() -> list[object]:

    """
    Makes functions calls to get_artist_data, get_album_data, get_album_tracks, and get_track_features in get_data.py
        de-dupes each resulting dataframe. Prints a message and dataframe head() upon completion.

    :return
        List: a list of tuples containing a dataframe and corresponding table name.
    """

    artists_df = get_artist_data(input_data)
    dedupe_data(artists_df, "artists_df")
    print(f"Loaded artists {artists_df.head(1)}")

    albums_df = get_album_data(artists_df)
    dedupe_data(albums_df, "albums_df")
    print(f"Loaded albums {albums_df.head(1)}")

    tracks_df = get_album_tracks(albums_df)
    dedupe_data(tracks_df, "tracks_df")
    print(f"Loaded tracks {tracks_df.head(1)}")

    track_features_df = get_track_features(tracks_df)
    dedupe_data(track_features_df, "track_features_df")
    print(f"Loaded features {track_features_df.head(1)}")

    return [
        (artists_df, "artist"),
        (albums_df, "album"),
        (tracks_df, "track"),
        (track_features_df, "track_feature")
    ]


def main():
    """
    Makes functions calls to create tables, ingest, and load_dfs and create_views.

    :return:
        None
    """
    create_tables(create_table_stmts, DB_NAME)
    print(f"Created tables")

    tables = ingest()
    print("Inserting data frames")

    load_dfs(tables, DB_NAME)
    print("Insertion completed")

    create_views(create_view_stmts, DB_NAME)
    print("Views saved")


if __name__ == "__main__":
    main()
