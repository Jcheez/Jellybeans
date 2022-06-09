class _Negativecycle(Exception):
    '''
    An exception that will be called when a graph exhibits characteristics of negative weight cycles.
    '''
    def __init__(self, message):
        super().__init__(message)