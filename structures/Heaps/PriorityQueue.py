from math import floor
from typing import Any, Callable
from Jellybeans.exceptions.NotOneBasedIndexed import _NotOneBasedIndexed

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
        self.__pos = {}
        for x in range(1, len(self.__container)):
            self.__addIndex(x)

        self.__quickTidy()

    def __addIndex(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION
        '''
        if str(self.__container[idx]) in self.__pos:
            sett = self.__pos[str(self.__container[idx])]
            sett.add(idx)
        else:
            self.__pos[str(self.__container[idx])] = {idx}

    def __updateIndex(self, old_idx:int, new_idx:int) -> None:
        '''
        INTERNAL FUNCTION
        '''
        if self.__container[old_idx] != self.__container[new_idx]:
            self.__pos[str(self.__container[new_idx])].remove(old_idx)
            self.__pos[str(self.__container[new_idx])].add(new_idx)

    def __removeIndex(self, item:Any, index:int) -> None:
        if len(self.__pos[str(item)]) > 1:
            self.__pos[str(item)].remove(index)
        else:
            del self.__pos[str(item)]

    def __shiftUp(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION
        Conduct shiftups on a node so that heap property is not violated
        '''
        while idx > 1 and self.__comparator(self.__container[idx], self.__container[self.__parent(idx)]):
            self.__container[idx], self.__container[self.__parent(idx)] = self.__container[self.__parent(idx)], self.__container[idx], 
            self.__updateIndex(self.__parent(idx), idx)
            self.__updateIndex(idx, self.__parent(idx))
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
                self.__container[idx], self.__container[currIdx] = self.__container[currIdx],  self.__container[idx]
                self.__updateIndex(currIdx, idx)
                self.__updateIndex(idx, currIdx)
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
        self.__addIndex(self.__size)
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
        
        self.__addIndex(1)
        
        self.__size -= 1
        self.__container.pop()
        self.__removeIndex(result, 1)
        self.__shiftDown(1)
        return result

    def sort(self) -> list:
        '''
        Returns a sorted list according to the rules of the comparator
        '''
        result = []
        for _ in range(self.__size):
            result.append(self.extract())
        return result

    def isEmpty(self) -> bool:
        return self.__size == 0

    def search(self, item:Any) -> bool:
        return str(item) in self.__pos

    def update(self, item:Any, new_item:Any) -> None:
        if str(item) not in self.__pos:
            raise KeyError(f"{item} not found in Heap")
        idx_item = min(self.__pos[str(item)])
        self.__container[idx_item] = new_item
        self.__removeIndex(item, idx_item)
        self.__addIndex(idx_item)
        self.__shiftUp(idx_item)
        self.__shiftDown(idx_item)
        return idx_item

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