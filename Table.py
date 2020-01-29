import sqlite3


class Table:

    def __init__(self, name, connection, columns, **kwargs):
        self.name = name
        self.connection = connection
        self.column_data = columns
        self.cursor = self.connection.sqlite_connection.cursor()

    def __iter__(self):
        self.cursor.execute('SELECT * FROM {}'.format(self.name))
        return self

    def __next__(self):
        # extract row and build Relation object
        pass

    def insert(self, *args, **kwargs):
        pass




