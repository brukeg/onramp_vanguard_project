import pandas as pd


def list_to_dataframe(func):

    def wrapper(data: list):
        list_dicts = func(data)

        return pd.DataFrame.from_dict(list_dicts)

    return wrapper


def dedupe_data(dataframe: object, filter: str):

    subset_filters = {
        "artists_df": ['name'],
        "albums_df": ['album_name'],
        "tracks_df": ['song_name', 'explicit'],
        "track_features_df": ['track_id', 'song_uri']
    }

    subset = subset_filters[filter]

    return dataframe.drop_duplicates(subset=subset, inplace=True, ignore_index=True)

# with subsets... none: 288, track id: 286 , song_uri: 286
