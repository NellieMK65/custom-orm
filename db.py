import sqlite3

# create a connection to the db
conn = sqlite3.connect("db.sqlite3")

# in order to execute sql queries, we need a cursor
cursor = conn.cursor()
