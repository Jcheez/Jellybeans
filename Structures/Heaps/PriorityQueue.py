from math import floor
from typing import Any, Callable
from ...Algos.privateFuncs import swap
from .NotOneBasedIndexed import _NotOneBasedIndexed

class PriorityQueue:
    '''
    PriorityQueue is a binary heap
    Default: MaxHeap
    '''
    def __init__(self, arr:list = None, comparator:Callable = lambda x, y: x >=y) -> None:
        if type(arr) != list and arr != None:
            raise Exception("parameter arr must be of type list")
        elif arr != None and (len(arr) == 0 or arr[0] != None):
            raise _NotOneBasedIndexed("Input is not a one based Indexed list")
        
        self.__size = 0 if arr is None else len(arr) - 1
        self.__container = [None] if arr is None else arr
        self.__comparator = comparator

        self.__quickTidy()

    def __shiftUp(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION
        Conduct shiftups on a node so that heap property is not violated
        '''
        while idx > 1 and self.__comparator(self.__container[idx], self.__container[self.__parent(idx)]):
            swap(self.__container, idx, self.__parent(idx))
            idx = self.__parent(idx)

    def __shiftDown(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION
        Conduct shiftdowns on a node so that heap property is not violated
        '''
        while idx <= self.__size:
            currIdx = idx
            currNode = self.__container[idx]
            if self.__left(idx) <= self.__size and self.__comparator(self.__container[self.__left(idx)], currNode):
                currIdx = self.__left(idx)
                currNode = self.__container[self.__left(idx)]

            if self.__right(idx) <= self.__size and self.__comparator(self.__container[self.__right(idx)], currNode):
                currIdx = self.__right(idx)
                currNode = self.__container[self.__right(idx)]

            if (currIdx != idx):
                swap(self.__container, idx, currIdx)
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

    def __quickTidy(self) -> None:
        for idx in range(self.__parent(self.__size), 0, -1):
            self.__shiftDown(idx)
    
    def insert(self, item:Any) -> None:
        '''
        Insert an item into the heap
        '''
        self.__size += 1
        self.__container.append(item)
        self.__shiftUp(self.__size)

    def peek(self) -> Any:
        '''
        Returns the root node of the heap
        '''
        return self.__container[1]

    def extract(self) -> Any:
        '''
        Returns and remove the root node of the heap
        '''
        result = self.__container[1]
        self.__container[1] = self.__container[self.__size]
        self.__size -= 1
        self.__container.pop()
        self.__shiftDown(1)
        return result

    def sort(self) -> list:
        '''
        Returns a sorted list according to the rules of the comparator
        '''
        result = []
        for i in range(self.__size):
            result.append(self.extract())
        return result

    def isEmpty(self) -> bool:
        return self.__size == 0

    def __len__(self) -> int:
        '''
        Returns the size of the heap
        '''
        return self.__size

    def __str__(self) -> str:
        '''
        Returns a string representation of the heap
        '''
        return str(self.__container.copy())