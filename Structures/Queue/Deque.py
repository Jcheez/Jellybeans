from Jellybeans.Structures import Queue

class Deque(Queue):

    def __init__(self):
        super().__init__()

    def enqueue_front(self, item):
        '''
        Add an item to the front of the queue
        '''
        self._size += 1
        self._queue.addFront(item)