from typing import Any
from Jellybeans.Structures import TailedLinkedList


class Queue:
    '''
    Queue is a FIFO Data structure
    '''
    def __init__(self):
        self._size = 0
        self._queue = TailedLinkedList()

    def isEmpty(self) -> bool:
        '''
        Returns whether a queue is empty
        '''
        return self._size == 0

    def peek(self) -> Any:
        '''
        Returns the element at the front of the queue
        '''
        if self.isEmpty():
            return None
        return self._queue.get(0)

    def dequeue(self) -> Any:
        '''
        Returns and remove the element at the front of the queue
        '''
        if self._size == 0:
            raise IndexError("No item available for removal")
        self._size -= 1
        val = self._queue.get(0)
        self._queue.removeFront()
        return val

    def enqueue(self, item:Any) -> None:
        '''
        Add an item to the back of the queue
        '''
        self._size += 1
        self._queue.addBack(item)

    def __len__(self) -> int:
        '''
        Returns the size of the queue
        '''
        return self._size

    def __str__(self) -> str:
        '''
        Visual Representation of the queue
        '''
        if self._size == 0:
            return []
        return " -> ".join(self._queue.map(lambda x: str(x)).to_list())
