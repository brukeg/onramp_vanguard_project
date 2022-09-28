from submission.spotify_ingest_data.get_data import *

import os
import spotipy
from dotenv import load_dotenv

from spotipy.oauth2 import SpotifyClientCredentials
from submission.spotify_process_data.process_data import list_to_dataframe, dedupe_data
from submission.spotify_ingest_data.get_data import *
import pprint


load_dotenv('/Users/brukegetachew/Projects/onramp_vanguard_project/.env')
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

spotify = spotipy.Spotify(auth_manager=auth_manager)
# input_data = ["foo fighters", "the roots", "a tribe called quest"]
input_data = ["the roots"]


def get_artist_top_tracks(dataframe: object):
    top_tracks = []
    artist_ids = dataframe["uri"]
    for artist_id in artist_ids:
        print(artist_id)
        results = spotify.artist_top_tracks(artist_id=artist_id, country='US')
        tracks = results["tracks"]
        pprint.pprint(tracks)
        # if len(tracks) > 0:
        #     for
        #     top_tracks_dict = {}
        #     top_tracks_dict["track_id"] = tracks["id"]
        #     top_tracks_dict["popularity"] = tracks["popularity"]
        #     top_tracks.append(top_tracks_dict)

    print(top_tracks)
    return top_tracks

get_artist_top_tracks(roots_df)