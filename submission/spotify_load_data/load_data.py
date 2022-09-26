import sqlite3

conn = sqlite3.connect('spotify.db')
c = conn.cursor()

c.execute('DROP TABLE test_database')
conn.commit()
conn.close()