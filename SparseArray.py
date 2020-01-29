from Table import Table


class SparseArray(Table):

    def __init__(self, name, connection, columns, create_new, **kwargs):
        self.name = name
        self.connection = connection
        self.column_data = columns
        self.cursor = self.connection.sqlite_connection.cursor()

        #TODO: check connection and throw errors

