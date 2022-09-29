# import dataclasses

from submission.spotify_ingest_data.get_data import *
from submission.spotify_load_data.load_data import *
from submission.spotify_process_data.process_data import dedupe_data

DB_NAME = "/Users/brukegetachew/Projects/onramp_vanguard_project/submission/spotify.db"


def ingest() -> list[object]:
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


def load_views():
    pass


def main():
    create_tables(create_table_stmts, DB_NAME)
    print(f"Created tables")

    # Load data
    tables = ingest()
    print("Inserting data frames")

    load_dfs(tables, DB_NAME)
    print("Insertion completed")

    create_views(create_view_stmts, DB_NAME)
    print("Views saved")


if __name__ == "__main__":
    main()
