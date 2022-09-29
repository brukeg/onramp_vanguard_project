import pandas as pd


"""
Defines a decorator used in get_data.py.
Transforms data through de-duping.
"""


def list_to_dataframe(func: object):
    """
    Decorates each function in get_data.py. Turns a list of dicts into a Pandas Dataframe.

    :param
        func (object): function to decorate.

    :return
        Dataframe: a new dataframe
    """
    def wrapper(data: list):
        list_dicts = func(data)

        return pd.DataFrame.from_dict(list_dicts)

    return wrapper


def dedupe_data(dataframe: object, s_filter: str):
    """
    Removes duplicates in a Pandas dataframe. Uses the subset param to identify which column(s) to dedupe.

    :param
        dataframe (object): the dataframe to dedupe.
    :param
        s_filter (str): the column name to dedupe.

    :return
        Dataframe: a de-duped dataframe
    """
    subset_filters = {
        "artists_df": ['artist_name'],
        "albums_df": ['album_name'],
        "tracks_df": ['song_name', 'explicit'],
        "track_features_df": ['track_id', 'song_uri']
    }

    subset = subset_filters[s_filter]

    return dataframe.drop_duplicates(subset=subset, inplace=True, ignore_index=True)
