from __future__ import annotations
from typing import Any, Callable
from .linked_list import LinkedList
from .doubly_node import _DoublyNode

class DoublyLinkedList(LinkedList):
    '''
    Doubly Linked List
    '''
    def __init__(self, items:Any=None):
        '''
        Args:
            item: either None, 1 item, or a list/tuple of items
        '''
        self.__tail = None
        super().__init__(items)

    def add_front(self, item:Any) -> LinkedList:
        '''
        Adds the item to the front of the DoublyLinkedList

        Args:
            item: Item to be added at the front of the DoublyLinkedList
        Returns:
            The updated DoublyLinkedList
        '''
        new_node = _DoublyNode(item, self._LinkedList__head)
        self._LinkedList__head = new_node
        if self._LinkedList__head.next() != None:
            new_node.next().set_prev(new_node)
        if self.__tail == None:
            self.__tail = new_node
        self._LinkedList__size += 1
        return self

    def add_back(self, item:Any) -> DoublyLinkedList:
        '''
        Adds the item to the back of the DoublyLinkedList

        Args:
            item: Item to be added at the back of the DoublyLinkedList
        Returns:
            The updated DoublyLinkedList
        '''
        new_node = _DoublyNode(item)

        if self._LinkedList__head == None:
            self._LinkedList__head = new_node
            self.__tail = new_node
        else:
            curr_node = self._LinkedList__head
            while curr_node.next() != None:
                curr_node = curr_node.next()
            new_node.set_prev(curr_node)
            curr_node.set_next(new_node)
            self.__tail = new_node
        self._LinkedList__size += 1
        return self
    
    def add_at_index(self, item:Any, index:int) -> DoublyLinkedList:
        '''
        Adds the item at a specified index of the DoublyLinkedList

        Args:
            item: Item to be added
            index: position to add the item
        Returns:
            The updated LinkedList
        '''
        if index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index > self._LinkedList__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index == 0:
            self.add_front(item)
        elif index == self._LinkedList__size:
            self.add_back(item)
        else:
            curr_node = self._LinkedList__head
            for _ in range(index-1):
                curr_node = curr_node.next()
            new_node = _DoublyNode(item, curr_node.next(), curr_node)
            curr_node.next().set_prev(new_node)
            curr_node.set_next(new_node)
            self._LinkedList__size += 1
        return self

    def remove_front(self) -> DoublyLinkedList:
        '''
        Remove the item at the front of the linked list

        Returns:
            The updated DoublyLinkedList
        '''
        if self._LinkedList__size == 1:
            self.__tail = None
        
        if self._LinkedList__size > 1:
            self._LinkedList__head.next().set_prev(None)
        return super().remove_front()

    def remove_back(self) -> DoublyLinkedList:
        '''
        Remove the item at the back of the DoublyLinkedList
        
        Returns:
            The updated DoublyLinkedList
        '''
        if self._LinkedList__size == 0:
            return self
        elif self._LinkedList__size == 1:
            self._LinkedList__head = None
            self.__tail = None
            self._LinkedList__size -= 1
            return self
        self.__tail = self.__tail.prev()
        self.__tail.set_next(None)
        self._LinkedList__size -= 1
        return self

    def remove_at_index(self, index:int) -> DoublyLinkedList:
        '''
        Remove an item from a specified index 

        Args:
            index: Index of item to remove
        Returns:
            The updated DoublyLinkedList
        '''
        if index == 0:
            return self.remove_front()
        elif index == self._LinkedList__size - 1:
            return self.remove_back()
        elif index >= self._LinkedList__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        else:
            curr_node = self._LinkedList__head
            for i in range(index - 1):
                curr_node = curr_node.next()
            curr_node.set_next(curr_node.next().next())
            curr_node.next().set_prev(curr_node)
            self._LinkedList__size -= 1
            return self

    def invert(self) -> DoublyLinkedList:
        '''
        Reverses the LL. 
        
        Returns:
            New inversed DoublyLinkedList 
        '''
        new_ll = DoublyLinkedList()
        curr_node = self.__tail
        while curr_node != None:
            new_ll.add_back(curr_node.get_item())
            curr_node = curr_node.prev()
        return new_ll

    def map(self, func:Callable[[Any], Any]) -> DoublyLinkedList:
        '''
        Maps the current LinkedList to a function. Returns a new DoublyLinkedList

        Args:
            func: A function to map the values by
        Returns:
            A new DoublyLinkedList containing the mapped values
        '''
        new_ll = DoublyLinkedList()
        curr_node = self._LinkedList__head

        while curr_node != None:
            new_ll.add_back(func(curr_node.get_item()))
            curr_node = curr_node.next()

        return new_ll

    def filter(self, func:Callable[[Any], Any]) -> DoublyLinkedList:
        '''
        Filter the Linkedlist based on a function. Returns a new DoublyLinkedlist

        Args:
            func: A function to filter the values by
        Returns:
            A new DoublyLinkedList containing the filtered values
        '''
        new_ll = DoublyLinkedList()
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