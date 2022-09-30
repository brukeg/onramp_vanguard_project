## Submission Readme

Use this file to explain what files are doing what.  Consider that the people grading this project might not be familiar with the way you chose to structure everything.  This should be a high level overview which can quickly get someone else up to speed and able to understand your code / submissions.

# Onramp: Vanguard Data Engineering Project

## Run Project: /submission
Contains the files `main.py`, `spotify.db`, and this `readme.md`. The file `main.py` is used to run the entire scrip with it's `main()` function. To kick off the project click "run main" (or similar) next to `if __name__ == "__main__"` in your IDE of choice. 

`main.py` establishes the file path to `spotify.db` with the constant `DB_NAME`. 
The function `ingest()` calls functions in `get_data.py` and `process_data.py` prior to invoking `main()`. 
`main.py` calls functions in `load_data.py` which creates tables and views and loads them with data.

### Extract Data: /spotify_ingest_data
Has one file: `get_data.py` which manages the connection to Spotify using a virtual environment. This file also instantiate a list of 21 artists (musicians or bands) to query Spotify for. Rather than picking my favorite artists or a random subset of artists I choose to ingest three distinct subgenres of artists: alternative metal, alternative hip hop, and alternative rock.
The functions in `get_data.py` query Spotify using the `spotipy` Python module and return a list of dictionaries containing metadata for each of the 4 tables: `artist`, `album`, `track`, and `track_feature`. 

### Transform: /spotify_process_data
Has one file: `process_data.py` with two functions for transforming the data returned in `get_data.py`. A decorator is defined as `list_to_dataframe()` and is subsequently used on each function in `get_data.py` because Pandas' `pd.drop_duplicates` method requires a dataframe object. The function for de-deuping data is defined as `dedupe_data()`, and this function is called in the `ingest()` function of `main.py`.

### Load: /spotify_load_data
In `load_data.py` SQL tables are created with Pandas' `pd.to_sql` method which takes a target dataframe object and inserts data into a database -> table. A context manager is used in functions which establish a connection to the database `spotify.db`. SQL statements are imported as modules for both tables and views: `create_table_stmts` and `create_view_stmts` respectively. 

For `create_tables()` table definition are read into `cur_execute()` for each of the four tables: `artist`, `album`, `track`, `track_features` using the list of table definitions in the variable `create_table_stmts`. 
In `insert_table_data()` data is inserted into the table definitions with Pandas' `pd.to_sql` method.
`load_dfs()` iterates through a list of tuples of the schema: (dataframe, table_name) and calls `insert_table_data()` to inserts data into the tables.
With `creates_views()` data in each of the four tables is used to create sql views defined in the variable `create_view_stmts`. 

#### Other Relevant Files
To run this project a `requirements.txt` file is provided.

## Views

### top_songs_duration
__Description:__ Top 10 songs by artist in terms of duration_ms. Ordered by artist ascending and duration_ms descending

__Columns__
- _artist_name:_ The name of the musician or band.
- _song_name_: The name of the song.
- _duration_ms_: The duration of the song in milliseconds

### top_artists
__Description:__ Top 20 artists in the database ordered by number of followers descending.

__Columns__
- _artist_name:_ The name of the musician or band.
- _followers_: The number of Spotify followers the artist has. 

### top_songs_tempo
__Description:__ Top 10 songs by artist in terms of tempo. Ordered by artist ascending and duration_ms descending)

__Columns__
- _artist_name:_ The name of the musician or band
- _song_name_: The name of the song.
- _tempo_: The overall estimated tempo of a track in beats per minute (BPM).

### artist_track_features
__Description:__ A wide view containing metadata (or features) about artists, albums, tracks, and track features ordered by artist_name ascending and release_date ascending.
A potential use could be for data scientists to explore with dimensionality reduction (like PCA) the potential for a small subset of features to predict the likelie that a given artist is popular.  

Detailed descriptions of column data can be found here: [Spotify.Tracks](https://hexdocs.pm/spotify_web_api/Spotify.Tracks.html#:~:text=of%20the%20track.-,The%20value%20will%20be%20between%200%20and%20100%2C%20with%20100,how%20recent%20those%20plays%20are.) 
and [Spotify.AudioFeatures](https://hexdocs.pm/spotify_web_api/Spotify.AudioFeatures.html#t:loudness/0)

__Columns__
- _artist_name:_ The name of the musician or band.
- _genre:_ A musical subgenre. One of: alternative metal, alternative hip hop, or alternative rock.
- _artist_popularity_: The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.
- _artist_followers_: The number of Spotify followers the artist has.
- _song_name_: The name of the song.
- _track_duration_ms_: The duration of the song in milliseconds.
- _explicit:_ A track with explicit lyrics: 1. 0 for no explicit lyrics.
- _track_type:_ The object type: `track`.
- _danceability_: How danceable a track is. A value of 0.0 is least danceable and 1.0 is most danceable.
- _energy:_ Measurement of intensity and activity. Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
- _instrumentalness_: Measurement of the likelihood the track is instrumental. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
- _liveness:_ Measurement of the likelihood the track is live. Detects the presence of an audience in the recording. A value above 0.8 provides strong likelihood that the track is live.
- _loudness:_ Relative Loudness of a track compared to other Spotify tracks. Values typical range between -60 and 0 db.
- _speechiness:_ The detected presence of speech in a track. The more exclusively speech-like the recording the closer to 1.0 the attribute value.
- _tempo:_ The overall estimated tempo of a track in beats per minute (BPM).
- _valence:_ The positiveness of a track. A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
- _track_feature_type:_ The object type: `audio_features`
- _release_date:_ An album release date (YYYY-MM-DD). 
- _album_name:_ The name of the musician or band.
- _album_type:_ The object type: `album`.

#### avg_loudness
__Description:__ A table containing genre, release date, and the average loudness of a given album. A potential use could be to see how loudness has changed over time overall or for a particular subgenre.

__Columns__
- _genre:_ A musical subgenre. One of: alternative metal, alternative hip hop, or alternative rock. 
- _release_date_: An album release date (YYYY-MM-DD).
- _avg_loudness_: An album's average loudness in db (-60 to 0).

## Data Visualization: /spotify_data_visualization
Contains four files: 
- `spotify_average_album_valance.py`: Plots the average valence per album for the band A Tribe Called Quest. 
- `spotify_average_loudness_by_year.py`: Plots the average loudness of a given album by release date and year.
- `spotify_top_ten_total_followers.py`: Plots the top 10 artists by number of followers.
- `visualization.pdf`: summarizes the findings.

To produce visualizations from the 3 `.py` files. you must run the files individually.
