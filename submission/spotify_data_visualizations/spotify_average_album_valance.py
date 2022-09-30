
import sqlite3
import pandas as pd
from pylab import *
from submission.main import DB_NAME

# SQL statement to execute
stmt = """
    SELECT album_name, valence
    FROM artist_track_features
    WHERE artist_name = 'A Tribe Called Quest';
"""

# data context manager
with sqlite3.connect(DB_NAME) as conn:
    df = pd.read_sql(stmt, conn)
conn.close()

# Calculate the mean of valence per album
mean_df = df.groupby("album_name").mean()
df = mean_df.reset_index()

# Replace album names with shorter album monikers
df["album_name"].replace(
    {"People's Instinctive Travels and the Paths of Rhythm (25th Anniversary Edition)": "People's Instinctive Travels",
     "We got it from Here... Thank You 4 Your service": "We got it from Here"
     },
    inplace=True
)

# Create a simple bar graph
df.plot(kind='bar', x='album_name', y='valence')
plt.ylim(.4, .8)

# Label the graph axes and title
plt.title("ATCQ Average Valence by Album")
plt.ylabel("Valence")
plt.xlabel("Album Name")

# Rotate x-axis labels by 45 degrees.
plt.xticks(rotation=45)

# Show plot
plt.show()


