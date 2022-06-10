from __future__ import annotations
from typing import Any, Callable, NewType, Union
from .node import _Node

class LinkedList:
    '''
    Single Linked List
    '''
    def __init__(self, item:Any = None):
        '''
        Args:
            item: either None, 1 item, or a list/tuple of items
        '''
        self.__head = None
        self.__size = 0
        if item == None:
            return
        
        if (type(item) == list or type(item) == tuple):
            for i in item:
                self.add_back(i)
        else:
            self.add_back(item)

    def add_front(self, item:Any) -> LinkedList:
        '''
        Adds the item to the front of the linkedList

        Args:
            item: Item to be added at the front of the linked list
        Returns:
            The updated LinkedList
        '''
        new_node = _Node(item, self.__head)
        self.__head = new_node
        self.__size += 1
        return self
        
    def add_back(self, item:Any) -> LinkedList:
        '''
        Adds the item to the back of the linkedlist

        Args:
            item: Item to be added at the back of the linked list
        Returns:
            The updated LinkedList
        '''
        new_node = _Node(item)

        if self.__head == None:
            self.__head = new_node
        else:
            curr_node = self.__head
            while curr_node.next() != None:
                curr_node = curr_node.next()
            curr_node.set_next(new_node)
        self.__size += 1
        return self
    
    def add_at_index(self, item:Any, index:int) -> LinkedList:
        '''
        Adds the item at a specified index of the linkedlist
        Args:
            item: Item to be added
            index: position to add the item
        Returns:
            The updated LinkedList
        '''
        if index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index > self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index == 0:
            self.add_front(item)
        elif index == self.__size:
            self.add_back(item)
        else:
            curr_node = self.__head
            for _ in range(index-1):
                curr_node = curr_node.next()
            new_node = _Node(item, curr_node.next())
            curr_node.set_next(new_node)
            self.__size += 1
        return self

    def remove_front(self) -> LinkedList:
        '''
        Remove the item at the front of the linked list

        Returns:
            The updated LinkedList
        '''
        if self.__size == 0:
            return self
        self.__head = self.__head.next()
        self.__size -= 1
        return self

    def remove_back(self) -> LinkedList:
        '''
        Remove the item at the back of the linked list

        Returns:
            The updated LinkedList
        '''
        if self.__size == 0:
            return self
        elif self.__size == 1:
            self.__head = None
            self.__size -= 1
        else:
            curr_node = self.__head
            for _ in range(self.__size - 2):
                curr_node = curr_node.next()
            curr_node.set_next(None)
            self.__size -= 1
        return self

    def remove_at_index(self, index:int) -> LinkedList:
        '''
        Remove an item from a specified index 

        Args:
            index: Index of item to remove
        Returns:
            The updated LinkedList
        '''
        if index == 0:
            return self.remove_front()
        elif index == self.__size - 1:
            return self.remove_back()
        elif index >= self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        else:
            curr_node = self.__head
            for _ in range(index - 1):
                curr_node = curr_node.next()
            curr_node.set_next(curr_node.next().next())
            self.__size -= 1
            return self

    def update(self, index: int, new_item:Any) -> LinkedList:
        '''
        Update the value of an item at a specified index

        Args:
            index: index to be updated
            newItem: Item to be inserted into the linkedlist
        Returns:
            The updated LinkedList
        '''
        curr_node = self.__head
        if curr_node == None:
            return self
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index >= self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        
        while index > 0:
            curr_node = curr_node.next()
            index -= 1
        curr_node.set_item(new_item)
        return self

    def get(self, index: int) -> Union[None, int]:
        '''
        Returns the item at a specified index

        Args:
            index: index of the item
        
        Returns:
            None if the LinkedList is empty else the item
        '''
        curr_node = self.__head
        if curr_node == None:
            return None
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index >= self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        
        while index > 0:
            curr_node = curr_node.next()
            index -= 1
        return curr_node.get_item()

    def map(self, func: Callable[[Any], Any]) -> LinkedList:
        '''
        Maps the current LinkedList to a function. Returns a new LinkedList

        Args:
            func: A function to map the values by
        Returns:
            A new LinkedList containing the mapped values
        '''
        new_ll = LinkedList()
        curr_node = self.__head

        while curr_node != None:
            new_ll.add_back(func(curr_node.get_item()))
            curr_node = curr_node.next()

        return new_ll

    def filter(self, func: Callable[[Any], Any]) -> LinkedList:
        '''
        Filter the Linkedlist based on a function. Returns a new Linkedlist

        Args:
            func: A function to filter the values by
        Returns:
            A new LinkedList containing the filtered values
        '''
        new_ll = LinkedList()
        curr_node = self.__head
        while curr_node != None:
            if func(curr_node.get_item()):
                new_ll.add_back(curr_node.get_item())
            curr_node = curr_node.next()

        return new_ll

    def to_list(self) -> list:
        '''
        Converts the LinkedList to a list

        Returns:
            A list containing the values in the LinkedList
        '''
        curr_node = self.__head
        result = []
        while curr_node != None:
            result.append(curr_node.get_item())
            curr_node = curr_node.next()
        return result

    def __len__(self) -> int:
        '''
        Returns the size of the linkedlist
        '''
        return self.__size

    def __str__(self) -> str:
        '''
        String Representation of the linkedlist
        '''
        currNode = self.__head
        items = []

        if currNode == None:
            return "[]"
        
        while currNode != None:
            items.append(str(currNode.get_item()))
            currNode = currNode.next()
        return " => ".join(items)

    def __eq__(self, other:LinkedList) -> bool:
        '''
        Tells whether two LinkedLists are equal
        '''
        if not isinstance(other, LinkedList):
            return False
        elif self.__size != len(other):
            return False

        curr1 = self.__head
        curr2 = other.__head

        while curr1 != None and curr2 != None:
            if curr1.get_item() != curr2.get_item():
                return False
            curr1 = curr1.next()
            curr2 = curr2.next()
        return True