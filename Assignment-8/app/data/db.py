import sqlite3
import os

DB_PATH = os.path.join("Assignment-8", "DATA", "Intelligence_platform.db")

def connect_database():
    """
    Create and return a connection to the SQLite database.
    If the database file does not exist, it will be created.
    """
    conn = sqlite3.connect(DB_PATH)
    return conn