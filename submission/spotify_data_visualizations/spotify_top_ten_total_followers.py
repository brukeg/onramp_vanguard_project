
import sqlite3
import pandas as pd
from pylab import *
from submission.main import DB_NAME

# SQL statement to execute
stmt = "SELECT * FROM top_artists LIMIT 10;"

# data context manager
with sqlite3.connect(DB_NAME) as conn:
    df = pd.read_sql(stmt, conn)
conn.close()

# Create a simple bar graph
df.plot(kind='bar', x='artist_name', y='followers')

# Format yaxis values
gca().yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

# Label the graph axes and title
plt.title("Top 10 Artists by total number of Spotify Followers")
plt.ylabel("Number of Spotify Followers")
plt.xlabel("Artist")

# Rotate x-axis labels by 45 degrees.
plt.xticks(rotation=45)

# Show plot
plt.show()


