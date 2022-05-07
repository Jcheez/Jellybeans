from math import floor
from typing import Any, Callable
from ...Algos.privateFuncs import swap
from .NotOneBasedIndexed import NotOneBasedIndexed

class PriorityQueue:
    '''
    PriorityQueue is a binary heap
    Default: MaxHeap
    '''
    def __init__(self, arr:list = [None], comparator:Callable = lambda x, y: x >=y) -> None:
        if arr[0] != None:
            raise NotOneBasedIndexed("Input is not a one based Indexed list")
        
        self._size = 0 if arr is None else len(arr) - 1
        self._container = arr
        self._comparator = comparator

        self.__quickTidy()
    
    def insert(self, item:Any) -> None:
        '''
        Insert an item into the heap
        '''
        self._size += 1
        self._container.append(item)
        self.__shiftUp(self._size)

    def peek(self) -> Any:
        '''
        Returns the root node of the heap
        '''
        return self._container[1]

    def extract(self) -> Any:
        '''
        Returns and remove the root node of the heap
        '''
        result = self._container[1]
        self._container[1] = self._container[self._size]
        self._size -= 1
        self._container.pop()
        self.__shiftDown(1)
        return result

    def sort(self) -> list:
        result = []
        for i in range(self._size):
            result.append(self.extract())
        return result

    def __shiftUp(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION
        Conduct shiftups on a node so that heap property is not violated
        '''
        while idx > 1 and self._comparator(self._container[idx], self._container[self.__parent(idx)]):
            swap(self._container, idx, self.__parent(idx))
            idx = self.__parent(idx)

    def __shiftDown(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION
        Conduct shiftdowns on a node so that heap property is not violated
        '''
        while idx <= self._size:
            currIdx = idx
            currNode = self._container[idx]
            if self.__left(idx) <= self._size and self._comparator(self._container[self.__left(idx)], currNode):
                currIdx = self.__left(idx)
                currNode = self._container[self.__left(idx)]

            if self.__right(idx) <= self._size and self._comparator(self._container[self.__right(idx)], currNode):
                currIdx = self.__right(idx)
                currNode = self._container[self.__right(idx)]

            if (currIdx != idx):
                swap(self._container, idx, currIdx)
                idx = currIdx
            else:
                break

    def __parent(self, i:int) -> int:
        '''
        INTERNAL FUNCTION
        Returns the index of the parent of the current node
        '''
        return floor(i/2)

    def __left(self, i:int) -> int:
        '''
        INTERNAL FUNCTION
        Returns the index of the left child of the current node
        '''
        return i*2

    def __right(self, i:int) -> int:
        '''
        INTERNAL FUNCTION
        Returns the index of the right child of the current node
        '''
        return i*2 + 1

    def __quickTidy(self):
        for idx in range(self.__parent(self._size), 0, -1):
            self.__shiftDown(idx)

    def __len__(self):
        '''
        Returns the size of the heap
        '''
        return self._size

    def __str__(self):
        '''
        Returns a string representation of the heap
        '''
        pass