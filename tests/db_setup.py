# -*- coding: utf-8 -*-
"""
    util.db_setup.py
    -----------
    Script for creating database and tables.
    
"""

import os
import sqlite3 as sql

def db_setup():
    print('Creating database "tembici-test.db"')
    
    os.system("rm -f tembici-test.db")
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
        update_date INTEGER NOT NULL,
        password TEXT NOT NULL
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

    # --- Creating "log" table ---
    print('Creating "log" table.')
    cursor.execute("""
    CREATE TABLE log (
        uuid TEXT(32) PRIMARY KEY,
        user_uuid TEXT(32) NOT NULL,
        date INTEGER NOT NULL,
        token TEXT NOT NULL,
        FOREIGN KEY(user_uuid) REFERENCES users(uuid)
    )
    """)

    # Excute everything and cease action
    conn.commit()
    conn.close()

if __name__ == '__main__':
    db_setup()