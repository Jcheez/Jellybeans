from typing import Any
from jellybeans.structures import TailedLinkedList

class Queue:
    '''
    Queue is a FIFO Data structure
    '''
    def __init__(self):
        self.__size = 0
        self.__queue = TailedLinkedList()

    def isEmpty(self) -> bool:
        '''
        Returns whether a queue is empty
        '''
        return self.__size == 0

    def peek(self) -> Any:
        '''
        Returns the element at the front of the queue
        '''
        if self.isEmpty():
            return None
        return self.__queue.get(0)

    def dequeue(self) -> Any:
        '''
        Returns and remove the element at the front of the queue
        '''
        if self.__size == 0:
            raise IndexError("No item available for removal")
        self.__size -= 1
        val = self.__queue.get(0)
        self.__queue.remove_front()
        return val

    def enqueue(self, item:Any) -> None:
        '''
        Add an item to the back of the queue
        '''
        self.__size += 1
        self.__queue.add_back(item)

    def __len__(self) -> int:
        '''
        Returns the size of the queue
        '''
        return self.__size

    def __str__(self) -> str:
        '''
        Visual Representation of the queue
        '''
        if self.__size == 0:
            return []
        return " -> ".join(self.__queue.map(lambda x: str(x)).to_list())
