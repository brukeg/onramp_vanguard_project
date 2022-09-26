from submission.spotify_ingest_data.get_data import *
import pandas as pd

input_data = ["foo fighters", "the roots", "a tribe called quest"]
# input_data = ["the roots"]

subset = {
    "artists": ['name'],
    "albums": ['album_name'],
    "tracks": ['song_name', 'explicit'],
    "track_features": ['track_id', 'song_uri']
}

def dedupe_data(func, dataframe, lists):
    pass

artists = get_artist_data(input_data)
artists_df = pd.DataFrame.from_dict(artists)
artists_df.drop_duplicates(subset=subset["artists"], inplace=True, ignore_index=True)

albums = get_album_data(artists)
albums_df = pd.DataFrame.from_dict(albums)
albums_df.drop_duplicates(subset=subset["albums"], inplace=True, ignore_index=True)
# print(albums_df.head(20))
# print(albums_df["album_name"])

tracks = get_album_tracks(albums)
tracks_df = pd.DataFrame.from_dict(tracks)
# print(tracks_df.head())
# tracks_df.sort_values(by=['album_id', 'song_name'], inplace=True, ignore_index=True)
tracks_df.drop_duplicates(subset=subset["tracks"], inplace=True, ignore_index=True)
print(tracks_df["song_name"])

track_features = get_track_features(tracks)
track_features_df = pd.DataFrame.from_dict(track_features)
# print(track_features_df.columns)
track_features_df.drop_duplicates(subset=subset["track_features"], inplace=True, ignore_index=True)
# print(track_features_df["song_uri"])

# with subsets... none: 288, track id: 286 , song_uri: 286