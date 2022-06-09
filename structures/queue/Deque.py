from typing import Any
from jellybeans.structures import Queue

class Deque(Queue):
    '''
    Deque is an extension of Queue, allowing addition of elements at the front of the queue
    '''
    def __init__(self):
        super().__init__()

    def enqueue_front(self, item:Any) -> None:
        '''
        Add an item to the front of the queue
        '''
        self._Queue__size += 1
        self._Queue__queue.addFront(item)