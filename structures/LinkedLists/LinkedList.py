from __future__ import annotations
from typing import Any, Callable, NewType, Union
from .Node import _Node

class LinkedList:
    '''
    Single Linked List
    '''
    def __init__(self, item:Any = None):
        '''
        Create a LinkedList with 0 items, i item of multiple items \n
        Args:
            item: either None, 1 item, or a list/tuple of items
        '''
        self.__head = None
        self.__size = 0
        if item == None:
            return
        
        if (type(item) == list or type(item) == tuple):
            for i in item:
                self.addBack(i)
        else:
            self.addBack(item)

    def addFront(self, item:Any) -> LinkedList:
        '''
        Adds the item to the front of the linkedList
        '''
        newNode = _Node(item, self.__head)
        self.__head = newNode
        self.__size += 1
        return self
        
    def addBack(self, item:Any) -> LinkedList:
        '''
        Adds the item to the back of the linkedlist
        '''
        newNode = _Node(item)

        if self.__head == None:
            self.__head = newNode
        else:
            currNode = self.__head
            while currNode.next() != None:
                currNode = currNode.next()
            currNode.setNext(newNode)
        self.__size += 1
        return self
    
    def addAtIndex(self, item:Any, index:int) -> LinkedList:
        '''
        Adds the item at a specified index of the linkedlist
        '''
        if index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index > self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index == 0:
            self.addFront(item)
        elif index == self.__size:
            self.addBack(item)
        else:
            currNode = self.__head
            for i in range(index-1):
                currNode = currNode.next()
            newNode = _Node(item, currNode.next())
            currNode.setNext(newNode)
            self.__size += 1
        return self

    def removeFront(self) -> LinkedList:
        '''
        Remove the item at the front of the linked list
        '''
        if self.__size == 0:
            return self
        self.__head = self.__head.next()
        self.__size -= 1
        return self

    def removeBack(self) -> LinkedList:
        '''
        Remove the item at the back of the linked list
        '''
        if self.__size == 0:
            return self
        elif self.__size == 1:
            self.__head = None
            self.__size -= 1
        else:
            currNode = self.__head
            for iter in range(self.__size - 2):
                currNode = currNode.next()
            currNode.setNext(None)
            self.__size -= 1
        return self

    def removeAtIndex(self, index) -> LinkedList:
        '''
        Remove an item from a specified index \n
        Args:
            index: Index of item to remove
        '''
        if index == 0:
            return self.removeFront()
        elif index == self.__size - 1:
            return self.removeBack()
        elif index >= self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        else:
            currNode = self.__head
            for i in range(index - 1):
                currNode = currNode.next()
            currNode.setNext(currNode.next().next())
            self.__size -= 1
            return self

    def update(self, index: int, newItem:Any) -> LinkedList:
        '''
        Update the value of an item at a specified index
        Args:
            index: index to be updated
            newItem: Item to be inserted into the linkedlist
        '''
        currNode = self.__head
        if currNode == None:
            return self
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index >= self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        
        while index > 0:
            currNode = currNode.next()
            index -= 1
        currNode.setItem(newItem)
        return self

    def get(self, index: int) -> Union[None, int]:
        '''
        Returns the item at a specified index
        '''
        currNode = self.__head
        if currNode == None:
            return None
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index >= self.__size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        
        while index > 0:
            currNode = currNode.next()
            index -= 1
        return currNode.getItem()

    def map(self, func: Callable[[Any], Any]) -> LinkedList:
        '''
        Maps the current LinkedList to a function. Returns a new LinkedList
        '''
        newLL = LinkedList()
        currNode = self.__head

        while currNode != None:
            newLL.addBack(func(currNode.getItem()))
            currNode = currNode.next()

        return newLL

    def filter(self, func: Callable[[Any], Any]) -> LinkedList:
        '''
        Filter the Linkedlist based on a function. Returns a new Linkedlist
        '''
        newLL = LinkedList()
        currNode = self.__head
        while currNode != None:
            if func(currNode.getItem()):
                newLL.addBack(currNode.getItem())
            currNode = currNode.next()

        return newLL

    def to_list(self) -> list:
        '''
        Converts the LinkedList to a list
        '''
        currNode = self.__head
        result = []
        while currNode != None:
            result.append(currNode.getItem())
            currNode = currNode.next()
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
            items.append(str(currNode.getItem()))
            currNode = currNode.next()
        return " => ".join(items)

    def __eq__(self, other:int) -> bool:
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
            if curr1.getItem() != curr2.getItem():
                return False
            curr1 = curr1.next()
            curr2 = curr2.next()
        return True