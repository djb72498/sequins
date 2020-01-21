

class ConnectionConfiguration:

    def __init__(self,
                 autocommit=False,
                 timeout=600):
        self.autocommit = autocommit
        self.timeout = timeout
