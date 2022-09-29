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