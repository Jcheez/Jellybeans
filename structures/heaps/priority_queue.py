from math import floor
from typing import Any, Callable
from jellybeans.exceptions.not_one_based_index import _NotOneBasedIndexed

class PriorityQueue:
    '''
    PriorityQueue is an implementation of the binary heap data structure
    Default: MaxHeap
    '''
    def __init__(self, arr:list = None, comparator:Callable = lambda x, y: x >=y) -> None:
        '''
        Args:
            list: list of elements to be included into the heap (One based index)
            comparator: Function used to decide the linear ordering of the elements
        '''
        if type(arr) != list and arr != None:
            raise Exception("parameter arr must be of type list")
        elif arr != None and (len(arr) == 0 or arr[0] != None):
            raise _NotOneBasedIndexed("Input is not a one based Indexed list")
        
        self.__size = 0 if arr is None else len(arr) - 1
        self.__container = [None] if arr is None else arr
        self.__comparator = comparator
        self.__pos = {} # Dictionary of elements to a set of indexes
        for x in range(1, len(self.__container)):
            self.__add_index(x)

        self.__quick_tidy()

    def __add_index(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION

        This is a utility function for adding an item and its index into self.__pos.

        Args:
            idx: The index of the item to be added
        '''
        if str(self.__container[idx]) in self.__pos:
            sett = self.__pos[str(self.__container[idx])]
            sett.add(idx)
        else:
            self.__pos[str(self.__container[idx])] = {idx}

    def __update_index(self, old_idx:int, new_idx:int) -> None:
        '''
        INTERNAL FUNCTION

        This is a utility function for updating the index of an item in self.__pos.

        Args:
            old_idx: The original index of the item to be updated
            new_idx: The new index of the item to be updated
        '''
        if self.__container[old_idx] != self.__container[new_idx]:
            self.__pos[str(self.__container[new_idx])].remove(old_idx)
            self.__pos[str(self.__container[new_idx])].add(new_idx)

    def __remove_index(self, item:Any, index:int) -> None:
        '''
        INTERNAL FUNCTION

        This is a utility function for removing the index of an item in self.__pos.

        Args:
            item: The item to remove in self.__pos
            new_idx: The index to be removed
        '''
        if len(self.__pos[str(item)]) > 1:
            self.__pos[str(item)].remove(index)
        else:
            del self.__pos[str(item)]

    def __shift_up(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION

        Conduct shiftups on a node so that heap property is not violated

        Args:
            idx: The index to conduct the shiftUp operation on
        '''
        while idx > 1 and self.__comparator(self.__container[idx], self.__container[self.__parent(idx)]):
            self.__container[idx], self.__container[self.__parent(idx)] = self.__container[self.__parent(idx)], self.__container[idx], 
            self.__update_index(self.__parent(idx), idx)
            self.__update_index(idx, self.__parent(idx))
            idx = self.__parent(idx)

    def __shift_down(self, idx:int) -> None:
        '''
        INTERNAL FUNCTION

        Conduct shiftdowns on a node so that heap property is not violated

        Args:
            idx: The index to conduct the shiftDown operation on
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
                self.__update_index(currIdx, idx)
                self.__update_index(idx, currIdx)
                idx = currIdx
            else:
                break

    def __parent(self, i:int) -> int:
        '''
        INTERNAL FUNCTION

        Args:
            index of the current node
        Returns:
            parent index of the current node
        '''
        return floor(i/2)

    def __left(self, i:int) -> int:
        '''
        INTERNAL FUNCTION

        Args:
            index of the current node
        Returns:
            left child of the current node
        '''
        return i*2

    def __right(self, i:int) -> int:
        '''
        INTERNAL FUNCTION

        Args:
            index of the current node
        Returns:
            right child of the current node
        '''
        return i*2 + 1

    def __quick_tidy(self) -> None:
        for idx in range(self.__parent(self.__size), 0, -1):
            self.__shift_down(idx)
    
    def insert(self, item:Any) -> None:
        '''
        Insert an item into the heap

        Args:
            item: item to be inserted into the heap
        '''
        self.__size += 1
        self.__container.append(item)
        self.__add_index(self.__size)
        self.__shift_up(self.__size)

    def peek(self) -> Any:
        '''
        Take a look at the root node of the heap

        Returns:
            root node of the heap
        '''
        return self.__container[1]

    def extract(self) -> Any:
        '''
        Returns and remove the root node of the heap

        Rerturns:
            value of the root node of the heap
        '''
        result = self.__container[1]
        self.__container[1] = self.__container[self.__size]
        
        self.__add_index(1)
        
        self.__size -= 1
        self.__container.pop()
        self.__remove_index(result, 1)
        self.__shift_down(1)
        return result

    def sort(self) -> list:
        '''
        Returns a sorted list according to the rules of the comparator

        Returns:
            list of the sorted elements
        '''
        result = []
        for _ in range(self.__size):
            result.append(self.extract())
        return result

    def is_empty(self) -> bool:
        '''
        Checks if the binary heap is empty
        
        Returns:
            True if heap is empty
        '''
        return self.__size == 0

    def search(self, item:Any) -> bool:
        '''
        Check if an item is present in the heap

        Args:
            item: Item to be found
        Returns:
            True if item is present
        '''
        return str(item) in self.__pos

    def update(self, item:Any, new_item:Any) -> None:
        '''
        Replace an item in the binary heap

        Args:
            item: The item to be replaced
            new_item: The new item
        '''
        if str(item) not in self.__pos:
            raise KeyError(f"{item} not found in Heap")
        idx_item = min(self.__pos[str(item)])
        self.__container[idx_item] = new_item
        self.__remove_index(item, idx_item)
        self.__add_index(idx_item)
        self.__shift_up(idx_item)
        self.__shift_down(idx_item)
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