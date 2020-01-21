import sqlite3

import ConnectionConfiguration.ConnectionConfiguration as cc


# Wraps a sqlite3 connection
class Connection:

    def __init__(self, dbname, autocommit=False, timeout=600):

        if dbname[-3:] != '.db':
            dbname = dbname + '.db'

        self.sqlite_connection = sqlite3.connect(dbname)
        self.config = ConnectionConfiguration(autocommit, timeout)

    def __enter__(self):
        pass

    def __exit(self):
        pass