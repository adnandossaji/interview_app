#!python3

# Create structured interview data database

import sqlite3
conn= sqlite3.connect( 'interview_app.db' )
conn.execute( """

CREATE TABLE User
(
    id INT PRIMARY KEY NOT NULL,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

""" )

conn.execute( """

CREATE UNIQUE INDEX User_username_uindex ON User (username);

""")

conn.execute( """

CREATE UNIQUE INDEX User_id_uindex ON User (id);

""")