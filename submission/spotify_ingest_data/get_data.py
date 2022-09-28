import os
import spotipy
from dotenv import load_dotenv

from spotipy.oauth2 import SpotifyClientCredentials
from submission.spotify_process_data.process_data import list_to_dataframe


load_dotenv('/Users/brukegetachew/Projects/onramp_vanguard_project/.env')
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

spotify = spotipy.Spotify(auth_manager=auth_manager)
input_data = ["foo fighters", "the roots", "a tribe called quest"]
# input_data = ["the roots"]


@list_to_dataframe
def get_artist_data(artists_list: list):
    """
    Artists
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
roots_df = get_artist_data(["the roots"])


@list_to_dataframe
def get_album_data(dataframe: object):
    """
    Albums
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
    Tracks
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
    Track Features
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
