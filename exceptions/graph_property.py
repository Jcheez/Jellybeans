class _GraphProperty(Exception):
    '''
    An exception that will be called when certain graph properties are being violated.
    '''
    def __init__(self, message):
        super().__init__(message)