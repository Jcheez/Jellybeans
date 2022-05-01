from __future__ import annotations
from typing import Any, Callable
from .LinkedList import LinkedList
from .DoublyNode import DoublyNode

class DoublyLinkedList(LinkedList):
    '''
    Doubly Linked List
    '''
    def __init__(self, items:Any=None):
        self._tail = None
        super().__init__(items)

    def addFront(self, item:Any) -> LinkedList:
        '''
        Adds the item to the front of the linkedList
        '''
        newNode = DoublyNode(item, self._head)
        self._head = newNode
        if self._head.next() != None:
            newNode.next().setPrev(newNode)
        if self._tail == None:
            self._tail = newNode
        self._size += 1
        return self

    def addBack(self, item:Any) -> DoublyLinkedList:
        '''
        Adds the item to the back of the linkedlist
        '''
        newNode = DoublyNode(item)

        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            currNode = self._head
            while currNode.next() != None:
                currNode = currNode.next()
            newNode.setPrev(currNode)
            currNode.setNext(newNode)
            self._tail = newNode
        self._size += 1
        return self
    
    def addAtIndex(self, item:Any, index:int) -> DoublyLinkedList:
        '''
        Adds the item at a specified index of the linkedlist
        '''
        if index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index > self._size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index == 0:
            self.addFront(item)
        elif index == self._size:
            self.addBack(item)
        else:
            currNode = self._head
            for i in range(index-1):
                currNode = currNode.next()
            newNode = DoublyNode(item, currNode.next(), currNode)
            currNode.next().setPrev(newNode)
            currNode.setNext(newNode)
            self._size += 1
        return self

    def removeFront(self) -> DoublyLinkedList:
        '''
        Remove the item at the front of the linked list
        '''
        if self._size == 1:
            self._tail = None
        
        if self._size > 1:
            self._head.next().setPrev(None)
        return super().removeFront()

    def removeBack(self) -> DoublyLinkedList:
        '''
        Remove the item at the back of the linked list
        '''
        if self._size == 0:
            return self
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size -= 1
            return self
        self._tail = self._tail.prev()
        self._tail.setNext(None)
        self._size -= 1
        return self

    def removeAtIndex(self, index:int) -> DoublyLinkedList:
        '''
        Remove an item from a specified index \n
        Args:
            index: Index of item to remove
        '''
        if index == 0:
            return self.removeFront()
        elif index == self._size - 1:
            return self.removeBack()
        elif index >= self._size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        else:
            currNode = self._head
            for i in range(index - 1):
                currNode = currNode.next()
            currNode.setNext(currNode.next().next())
            currNode.next().setPrev(currNode)
            self._size -= 1
            return self

    def invert(self):
        '''
        Reverses the LL. Returns a new LinkedList
        '''
        newLL = DoublyLinkedList()
        currNode = self._tail
        while currNode != None:
            newLL.addBack(currNode.getItem())
            currNode = currNode.prev()
        return newLL

    def map(self, func:Callable[[Any], Any]) -> DoublyLinkedList:
        '''
        Maps the current LinkedList to a function. Returns a new DoublyLinkedList
        '''
        newLL = DoublyLinkedList()
        currNode = self._head

        while currNode != None:
            newLL.addBack(func(currNode.getItem()))
            currNode = currNode.next()

        return newLL

    def filter(self, func:Callable[[Any], Any]) -> DoublyLinkedList:
        '''
        Filter the Linkedlist based on a function. Returns a new DoublyLinkedlist
        '''
        newLL = DoublyLinkedList()
        currNode = self._head
        while currNode != None:
            if func(currNode.getItem()):
                newLL.addBack(currNode.getItem())
            currNode = currNode.next()

        return newLL