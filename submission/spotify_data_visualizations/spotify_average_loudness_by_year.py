
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
from submission.main import DB_NAME

# SQL statement to execute
stmt = "SELECT * FROM avg_loudness;"

# data context manager
with sqlite3.connect(DB_NAME) as conn:
    df = pd.read_sql(stmt, conn)
conn.close()

# Flip loudness from negative to positive numbers for readability
df['avg_loudness'] = df['avg_loudness'] * -1

# Create date format
format = '%Y-%m-%d'

# Format dates from strings to datetime
df['release_date'] = pd.to_datetime(df['release_date'], format=format, errors='ignore')

# Subset of dataframes by subgenres
hip_hop = df[df["genre"] == "alternative hip hop"]
metal = df[df["genre"] == "alternative metal"]
rock = df[df["genre"] == "alternative rock"]

# Instantiate figure and axes objects
fig, ax = plt.subplots()

# Load data into multiple axes.
ax.scatter(x=hip_hop["release_date"], y=hip_hop["avg_loudness"], color='red', label="hip hop")
ax.scatter(x=metal["release_date"], y=metal["avg_loudness"], color='blue', label="metal")
ax.scatter(x=rock["release_date"], y=rock["avg_loudness"], color='black', label="rock")

# title figure and axes, then add a legend, and finally show plot.
plt.title("Average Relative Album Loudness")
plt.ylabel("Relative Decibel (Db)")
plt.xlabel("Year")
ax.legend()
plt.show()
