import os
import spotipy
from dotenv import load_dotenv

from spotipy.oauth2 import SpotifyClientCredentials
from submission.spotify_process_data.process_data import list_to_dataframe


""" 
Manages the connection to Spotify through the use of a virtual environment.
"""
load_dotenv('/Users/brukegetachew/Projects/onramp_vanguard_project/.env')
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

spotify = spotipy.Spotify(auth_manager=auth_manager)

"""
Instantiates a list of artists to query Spotify for.
"""
input_data = [
    "foo fighters", "korn", "disturbed", "papa roach", "slipknot", "tool", "rob zombie",
    "the roots", "a tribe called quest", "j dilla", "common", "talib kweli", "mos def",
    "de la soul",
    "jack white", "radiohead", "the black keys", "red hot chili peppers", "weezer",
    "the decemberists", "the killers"
]

"""
Begin queries to Spotify.
"""
@list_to_dataframe
def get_artist_data(artists_list: list):
    """
    Queries Spotify for each artist in artists_lists. Puts relevant data in a dict for each artist,
        and appends each dict to a list called artists.

    :param
        artists_list (list): a list of strings containing artist names in lower case.
            for our purposes this is the variable "input_data"

    :return
        List: a list of dicts containing artist metadata
    """
    artists = []
    for artist in artists_list:
        results = spotify.search(q='artist:' + artist, type='artist')
        items = results["artists"]["items"]
        if len(items) > 0:
            artists_dict = {}
            artist = items[0]
            artists_dict["artist_id"] = artist["id"]
            artists_dict["artist_name"] = artist["name"]
            artists_dict["url"] = artist["external_urls"]["spotify"]
            artists_dict["genre"] = artist["genres"][0]
            artists_dict["image_url"] = artist["images"][0]["url"]
            artists_dict["followers"] = artist["followers"]["total"]
            artists_dict["popularity"] = artist["popularity"]
            artists_dict["type"] = artist["type"]
            artists_dict["uri"] = artist["uri"]
            artists.append(artists_dict)

    return artists


@list_to_dataframe
def get_album_data(dataframe: object):
    """
    Queries Spotify for each artist's albums using the artist uri. Puts relevant data in a dict for each artist's album,
        and appends each dict to a list called albums.

    :param
        dataframe (object): a dataframe containing artist metadata derived from get_artists_data function
            and the decorator list_to_dicts.

    :return
        List: a list of dicts containing album metadata
    """
    albums = []
    artist_ids = dataframe["uri"]
    for artist_id in artist_ids:
        results = spotify.artist_albums(artist_id=artist_id, album_type='album', country='US')
        items = results["items"]
        if len(items) > 0:
            for idx, album_obj in enumerate(items):
                albums_dict = {}
                albums_dict["album_id"] = items[idx]["id"]
                albums_dict["album_name"] = items[idx]["name"]
                albums_dict["external_url"] = items[idx]["external_urls"]["spotify"]
                albums_dict["image_url"] = items[idx]["images"][0]["url"]
                albums_dict["release_date"] = items[idx]["release_date"]
                albums_dict["total_tracks"] = items[idx]["total_tracks"]
                albums_dict["type"] = items[idx]["type"]
                albums_dict["uri"] = items[idx]["uri"]
                albums_dict["artist_id"] = items[idx]["artists"][0]["id"]
                albums.append(albums_dict)

    return albums


@list_to_dataframe
def get_album_tracks(dataframe: object):
    """
    Queries Spotify for each album's track using album_id. Puts relevant data in a dict for each artist's
        album, and appends each dict to a list called tracks.

    :param
        dataframe (object): a dataframe containing album metadata derived from get_album_data function
            and the decorator list_to_dicts.

    :return
        List: a list of dicts containing track metadata
    """
    tracks = []
    album_ids = dataframe["album_id"]
    for album_id in album_ids:
        results = spotify.album_tracks(album_id=album_id, limit=50, market='US')
        items = results["items"]
        if len(items) > 0:
            for idx, track_obj in enumerate(items):
                tracks_dict = {}
                tracks_dict["track_id"] = items[idx]["id"]
                tracks_dict["song_name"] = items[idx]["name"]
                tracks_dict["external_url"] = items[idx]["external_urls"]["spotify"]
                tracks_dict["duration_ms"] = items[idx]["duration_ms"]
                tracks_dict["explicit"] = items[idx]["explicit"]
                tracks_dict["disc_number"] = items[idx]["disc_number"]
                tracks_dict["type"] = items[idx]["type"]
                tracks_dict["song_uri"] = items[idx]["uri"]
                tracks_dict["album_id"] = album_id
                tracks.append(tracks_dict)

    return tracks


@list_to_dataframe
def get_track_features(dataframe: object):
    """
    Queries Spotify for each track's track features using track_id. Puts relevant data in a dict for each
        tracks's track features, and appends each dict to a list called track_features.

    :param
        dataframe (object): a dataframe containing track metadata derived from get_album_data function
            and the decorator list_to_dicts.

    :return
        List: a list of dicts containing track feature metadata
    """
    track_features = []
    track_ids = dataframe["track_id"]
    for track_id in track_ids:
        results = spotify.audio_features([track_id])
        if len(results) > 0:
            for idx, track_features_obj in enumerate(results):
                track_features_dict = {}
                track_features_dict["track_id"] = track_id
                track_features_dict["danceability"] = results[idx]["danceability"]
                track_features_dict["energy"] = results[idx]["energy"]
                track_features_dict["instrumentalness"] = results[idx]["instrumentalness"]
                track_features_dict["liveness"] = results[idx]["liveness"]
                track_features_dict["loudness"] = results[idx]["loudness"]
                track_features_dict["speechiness"] = results[idx]["speechiness"]
                track_features_dict["tempo"] = results[idx]["tempo"]
                track_features_dict["type"] = results[idx]["type"]
                track_features_dict["valence"] = results[idx]["valence"]
                track_features_dict["song_uri"] = results[idx]["uri"]
                track_features.append(track_features_dict)

    return track_features
