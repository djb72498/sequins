import sqlite3
import ConnectionConfiguration

# Wraps a sqlite3 connection
class Connection:

    def __init__(self, dbname, autocommit=False, timeout=600):

        if dbname[-3:] != '.db':
            dbname = dbname + '.db'

        self.sqlite_connection = sqlite3.connect(dbname)
        self.config = ConnectionConfiguration(autocommit, timeout)
        self.connected = True

    def _table_exists(self, table_name):
        cursor = self.sqlite_connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        cursor.fetchall()

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def table(self):
        cursor = self.sqlite_connection.cursor()
