from __future__ import annotations
from typing import Any, Callable
from .linked_list import LinkedList
from .node import _Node

class TailedLinkedList(LinkedList):
    '''
    Tailed Linked List
    '''
    def __init__(self, items=None):
        '''
        Args:
            item: either None, 1 item, or a list/tuple of items
        '''
        self.__tail = None
        super().__init__(items)

    def add_front(self, item:Any) -> TailedLinkedList:
        '''
        Adds the item to the front of the TailedLinkedList

        Args:
            item: Item to be added at the front of the TailedLinkedList
        Returns:
            The updated TailedLinkedList
        '''
        new_node = _Node(item, self._LinkedList__head)
        self._LinkedList__head = new_node
        if self.__tail == None:
            self.__tail = new_node
        self._LinkedList__size += 1
        return self

    def add_back(self, item:Any) -> TailedLinkedList:
        '''
        Adds the item to the back of the TailedLinkedList

        Args:
            item: Item to be added at the back of the TailedLinkedList
        Returns:
            The updated TailedLinkedList
        '''
        new_node = _Node(item)

        if self._LinkedList__head == None:
            self._LinkedList__head = new_node
            self.__tail = new_node
        else:
            curr_node = self.__tail
            curr_node.set_next(new_node)
            self.__tail = new_node
        self._LinkedList__size += 1
        return self

    def remove_front(self) -> TailedLinkedList:
        '''
        Remove the item at the front of the TailedLinkedList

        Returns:
            The updated TailedLinkedList
        '''
        if self._LinkedList__size == 1:
            self.__tail = None
        return super().remove_front()

    def remove_back(self) -> TailedLinkedList:
        '''
        Remove the item at the back of the TailedLinkedList

        Returns:
            The updated TailedLinkedList
        '''
        if self._LinkedList__size == 0:
            return self
        elif self._LinkedList__size == 1:
            self._LinkedList__head = None
            self.__tail = None
            self._LinkedList__size -= 1
        else:
            curr_node = self._LinkedList__head
            for _ in range(self._LinkedList__size - 2):
                curr_node = curr_node.next()
            self.__tail = curr_node
            curr_node.set_next(None)
            self._LinkedList__size -= 1
        return self

    def remove_at_index(self, index) -> TailedLinkedList:
        '''
        Remove an item from a specified index 

        Args:
            index: Index of item to remove
        Returns:
            The updated TailedLinkedList
        '''
        if self._LinkedList__size == 1:
            self.__tail = None
        return super().remove_at_index(index)

    def map(self, func:Callable[[Any], Any]) -> TailedLinkedList:
        '''
        Maps the current LinkedList to a function. Returns a new TailedLinkedList

        Args:
            func: A function to map the values by
        Returns:
            A new TailedLinkedList containing the mapped values
        '''
        new_ll = TailedLinkedList()
        curr_node = self._LinkedList__head

        while curr_node != None:
            new_ll.add_back(func(curr_node.get_item()))
            curr_node = curr_node.next()

        return new_ll

    def filter(self, func:Callable[[Any], Any]) -> TailedLinkedList:
        '''
        Filter the Linkedlist based on a function. Returns a new TailedLinkedlist

        Args:
            func: A function to filter the values by
        Returns:
            A new TailedLinkedList containing the filtered values
        '''
        new_ll = TailedLinkedList()
        curr_node = self._LinkedList__head
        while curr_node != None:
            if func(curr_node.get_item()):
                new_ll.add_back(curr_node.get_item())
            curr_node = curr_node.next()

        return new_ll

    def get(self, index:int) -> int:
        '''
        Returns the item at a specified index

        Args:
            index: index of the item
        
        Returns:
            None if the LinkedList is empty else the item
        '''
        if index == self._LinkedList__size - 1:
            return None if self.__tail is None else self.__tail.get_item()
        return super().get(index)