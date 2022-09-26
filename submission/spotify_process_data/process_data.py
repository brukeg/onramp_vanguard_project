import sqlite3
from submission.spotify_ingest_data.get_data import *
import pandas as pd
# from sqlalchemy import create_engine


input_data = ["foo fighters", "the roots", "a tribe called quest"]
# input_data = ["the roots"]

subset = [
    ['name'],
    ['album_name'],
    ['song_name', 'explicit'],
    ['track_id', 'song_uri']
]


# def list_to_dataframe(data: list, func):
#     """
#     :param data: list  of dicts to turn into a dataframe.
#     :param func: function to use to transform data.
#     :return df: a dataframe.
#     """
#     df = pd.DataFrame.from_dict(func(data))
#     return df
#
#
# list_to_dataframe(input_data, get_artist_data)
# list_to_dataframe(artists, get_album_data)
# list_to_dataframe(albums, get_album_tracks)
# list_to_dataframe(tracks, get_track_features)


# def dedupe_data(df):
#     """
#     :param df: dataframe to deduplicate
#     :return df: the data is updated inplace.
#     """
#     for idx in range(len(subset)):
#         df.drop_duplicates(subset=subset[idx], inplace=True, ignore_index=True)
#     return df
#
# dedupe_data()

artists = get_artist_data(input_data)
artists_df = pd.DataFrame.from_dict(artists)
artists_df.drop_duplicates(subset=subset[0], inplace=True, ignore_index=True)

albums = get_album_data(artists)
albums_df = pd.DataFrame.from_dict(albums)
albums_df.drop_duplicates(subset=subset[1], inplace=True, ignore_index=True)
# print(albums_df.head(20))
# print(albums_df["album_name"])

tracks = get_album_tracks(albums)
tracks_df = pd.DataFrame.from_dict(tracks)
# print(tracks_df.head())
# tracks_df.sort_values(by=['album_id', 'song_name'], inplace=True, ignore_index=True)
tracks_df.drop_duplicates(subset=subset[2], inplace=True, ignore_index=True)
# print(tracks_df["song_name"])

track_features = get_track_features(tracks)
track_features_df = pd.DataFrame.from_dict(track_features)
# print(track_features_df.columns)
track_features_df.drop_duplicates(subset=subset[3], inplace=True, ignore_index=True)
# print(track_features_df["song_uri"])

# with subsets... none: 288, track id: 286 , song_uri: 286
# artists_df, albums_df, tracks_df, track_features_df

conn = sqlite3.connect('spotify.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS artists ('
          'artist_id varchar(50), artist_name varchar(255), external_url varchar(100), genre varchar(100),'
          'image_url varchar(100), followers int, popularity int, type varchar(50), '
          'artist_uri varchar(100))'
          )
conn.commit()

artists_df.to_sql('artists', conn, if_exists='replace')

c.execute('''SELECT * FROM artists''')

for row in c.fetchall():
    print(row)
conn.close()
