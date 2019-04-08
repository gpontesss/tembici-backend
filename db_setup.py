import sqlite3 as sql

conn = sql.connect('db/users.db')
conn.close()