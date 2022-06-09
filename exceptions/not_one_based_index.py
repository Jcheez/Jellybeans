class _NotOneBasedIndexed(Exception):
    '''
    An exception that will be called when a Heap takes in a sequence which is not one base indexed.
    '''
    def __init__(self, message):
        super().__init__(message)