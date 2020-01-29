


class ColumnData:

    def __init__(self, **kwargs):

        self.labels = []
        self.types = []
        for key in kwargs.keys():
            self.labels.append(key)
            self.types.append(kwargs[key])

    def change_labels(self, **kwargs):
        pass

    def change_types(self, **kwargs):
        pass

    def add(self, **kwargs):
        pass

    def rm(self, *args):
        pass

