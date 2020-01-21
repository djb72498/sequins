import sqlite3


class Table:

    def __init__(self, name, connection, **kwargs):
        self.name = name
        self.connection = connection
        self.column_data

