import sqlite3 as sql
import uuid
from hashlib import sha256

print('Creating database "tembici-test.db"')
conn = sql.connect('tembici-test.db')

cursor = conn.cursor()

# --- Creating "users" table ---
print('Creating "users" table.')
cursor.execute("""
CREATE TABLE users (
    uuid TEXT(32) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    creation_date INTEGER NOT NULL,
    update_date INTEGER NOT NULL
)
""")

# --- Creating "phones" table ---
print('Creating "phones" table.')
cursor.execute("""
CREATE TABLE phones (
    uuid TEXT(32) PRIMARY KEY,
    user_uuid TEXT(32) NOT NULL,
    phone TEXT(16) NOT NULL,
    ddd TEXT(2) NOT NULL,
    FOREIGN KEY(user_uuid) REFERENCES users(uuid)
)
""")

# --- Creating "password" table ---
cursor.execute("""
CREATE TABLE password (
    uuid TEXT(32) PRIMARY KEY,
    user_uuid TEXT(32) NOT NULL,
    hash_password TEXT(64) NOT NULL,
    FOREIGN KEY(user_uuid) REFERENCES users(uuid)
)
""")

# Registering data
conn.commit()

conn.close()