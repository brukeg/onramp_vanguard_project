## Submission Readme

Use this file to explain what files are doing what.  Consider that the people grading this project might not be familiar with the way you chose to structure everything.  This should be a high level overview which can quickly get someone else up to speed and able to understand your code / submissions.

# Onramp: Vanguard Data Engineering Project

## Run Project: /submission
Starting with the directory: /submission which contains the files `main.py`, `spotify.db`, and this `readme.md`.

The file `main.py` is used to run the entire scrip with it's `def main()` function. To kick off the project click "run main" (or similar) next to `if __name__ == "__main__"` in your IDE of choice. `main.py` also establishes the file path to `spotify.db` with the constant `DB_NAME`. Lastly, the function `ingest()` makes calls to functions in /spotify_ingest_data prior to invoking `main()`. 

### Extract Data: /spotify_ingest_data
/spotify_ingest_data has one file: `get_data.py` which manages the connection to Spotify using a virtual environment. This file also instantiate a list of 21 artists (musicians or bands) to query Spotify for. Rather than picking my favorite artists or a random subset of artists I choose to ingest three distinct subgenres of artists: alternative metal, alternative hip hop, and alternative rock.
The functions in `get_data.py` query Spotify using the `spotipy` Python module and return a list of dictionaries containing metadata for each of the 4 tables: `artist`, `album`, `track`, and `track_feature`. 

### Transform: /spotify_process_data
process_data.py

### Load: /spotify_load_data
load_data.py

Other Relevant Files
requirements.txt