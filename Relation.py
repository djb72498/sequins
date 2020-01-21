


class Relation:

    def __init__(self, parent, **argv):

        self.parent = parent
        for key in argv.keys():
            self.__setattr__(key, argv[key])

        