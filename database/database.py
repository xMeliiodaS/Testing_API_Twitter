import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_file):
        """Initialize the Database class with the database file path."""
        self.db_file = db_file
        self.conn = None

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"Connected to SQLite database {self.db_file}")
        except Error as e:
            print(e)

    def execute_query(self, query, params=()):
        """Execute a query with optional parameters."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            return cursor
        except Error as e:
            print(e)
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Connection to SQLite database closed")
