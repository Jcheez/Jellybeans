from __future__ import annotations
from typing import Any, Callable
from .LinkedList import LinkedList
from .Node import Node

class TailedLinkedList(LinkedList):
    '''
    Tailed Linked List
    '''
    def __init__(self, items=None):
        self._tail = None
        super().__init__(items)

    def addFront(self, item:Any) -> TailedLinkedList:
        '''
        Adds the item to the front of the TailedLinkedList
        '''
        newNode = Node(item, self._head)
        self._head = newNode
        if self._tail == None:
            self._tail = newNode
        self._size += 1
        return self

    def addBack(self, item:Any) -> TailedLinkedList:
        '''
        Adds the item to the back of the TailedLinkedList
        '''
        newNode = Node(item)

        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            currNode = self._head
            while currNode.next() != None:
                currNode = currNode.next()
            currNode.setNext(newNode)
            self._tail = newNode
        self._size += 1
        return self

    def removeFront(self) -> TailedLinkedList:
        '''
        Remove the item at the front of the TailedLinkedList
        '''
        if self._size == 1:
            self._tail = None
        return super().removeFront()

    def removeBack(self) -> TailedLinkedList:
        '''
        Remove the item at the back of the TailedLinkedList
        '''
        if self._size == 0:
            return self
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size -= 1
        else:
            currNode = self._head
            for iter in range(self._size - 2):
                currNode = currNode.next()
            self._tail = currNode
            currNode.setNext(None)
            self._size -= 1
        return self

    def removeAtIndex(self, index) -> TailedLinkedList:
        '''
        Remove an item from a specified index \n
        Args:
            index: Index of item to remove
        '''
        if self._size == 1:
            self._tail = None
        return super().removeAtIndex(index)

    def map(self, func:Callable[[Any], Any]) -> TailedLinkedList:
        '''
        Maps the current LinkedList to a function. Returns a new TailedLinkedList
        '''
        newLL = TailedLinkedList()
        currNode = self._head

        while currNode != None:
            newLL.addBack(func(currNode.getItem()))
            currNode = currNode.next()

        return newLL

    def filter(self, func:Callable[[Any], Any]) -> TailedLinkedList:
        '''
        Filter the Linkedlist based on a function. Returns a new TailedLinkedlist
        '''
        newLL = TailedLinkedList()
        currNode = self._head
        while currNode != None:
            if func(currNode.getItem()):
                newLL.addBack(currNode.getItem())
            currNode = currNode.next()

        return newLL

    def get(self, index:int) -> int:
        if index == self._size - 1:
            return self._tail.getItem()
        return super().get(index)