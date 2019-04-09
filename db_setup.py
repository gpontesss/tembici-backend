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

mock_uuid = uuid.uuid4().hex
# Mock data for "users" table
print('Generating mock data for "users" table.')
cursor.execute("""
INSERT INTO users (uuid, name, email, creation_date, update_date)
VALUES ('{}', 'Guilherme Pontes', 'pontes.guisilva@gmail.com', date('now'), date('now'))
""".format(mock_uuid))

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

print('Generating mock data for "phones" table.')
cursor.execute("""
INSERT INTO phones (uuid, user_uuid, phone, ddd)
VALUES ('{}', '{}', '992139309', '11')
""".format(uuid.uuid4().hex, mock_uuid))

# --- Creating "password" table ---
cursor.execute("""
CREATE TABLE password (
    uuid TEXT(32) PRIMARY KEY,
    user_uuid TEXT(32) NOT NULL,
    hash_password TEXT(64) NOT NULL,
    FOREIGN KEY(user_uuid) REFERENCES users(uuid)
)
""")

print('Generating password for mock users.')
cursor.execute("""
INSERT INTO password (uuid, user_uuid, hash_password)
VALUES ('{}', '{}', '{}')
""".format(uuid.uuid4().hex, mock_uuid, sha256(b'secret').hexdigest()))

# Registering data
conn.commit()

conn.close()