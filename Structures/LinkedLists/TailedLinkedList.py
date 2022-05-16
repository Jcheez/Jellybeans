from __future__ import annotations
from typing import Any, Callable
from .LinkedList import LinkedList
from .Node import _Node

class TailedLinkedList(LinkedList):
    '''
    Tailed Linked List
    '''
    def __init__(self, items=None):
        self.__tail = None
        super().__init__(items)

    def addFront(self, item:Any) -> TailedLinkedList:
        '''
        Adds the item to the front of the TailedLinkedList
        '''
        newNode = _Node(item, self._LinkedList__head)
        self._LinkedList__head = newNode
        if self.__tail == None:
            self.__tail = newNode
        self._LinkedList__size += 1
        return self

    def addBack(self, item:Any) -> TailedLinkedList:
        '''
        Adds the item to the back of the TailedLinkedList
        '''
        newNode = _Node(item)

        if self._LinkedList__head == None:
            self._LinkedList__head = newNode
            self.__tail = newNode
        else:
            currNode = self._LinkedList__head
            while currNode.next() != None:
                currNode = currNode.next()
            currNode.setNext(newNode)
            self.__tail = newNode
        self._LinkedList__size += 1
        return self

    def removeFront(self) -> TailedLinkedList:
        '''
        Remove the item at the front of the TailedLinkedList
        '''
        if self._LinkedList__size == 1:
            self.__tail = None
        return super().removeFront()

    def removeBack(self) -> TailedLinkedList:
        '''
        Remove the item at the back of the TailedLinkedList
        '''
        if self._LinkedList__size == 0:
            return self
        elif self._LinkedList__size == 1:
            self._LinkedList__head = None
            self.__tail = None
            self._LinkedList__size -= 1
        else:
            currNode = self._LinkedList__head
            for iter in range(self._LinkedList__size - 2):
                currNode = currNode.next()
            self.__tail = currNode
            currNode.setNext(None)
            self._LinkedList__size -= 1
        return self

    def removeAtIndex(self, index) -> TailedLinkedList:
        '''
        Remove an item from a specified index \n
        Args:
            index: Index of item to remove
        '''
        if self._LinkedList__size == 1:
            self.__tail = None
        return super().removeAtIndex(index)

    def map(self, func:Callable[[Any], Any]) -> TailedLinkedList:
        '''
        Maps the current LinkedList to a function. Returns a new TailedLinkedList
        '''
        newLL = TailedLinkedList()
        currNode = self._LinkedList__head

        while currNode != None:
            newLL.addBack(func(currNode.getItem()))
            currNode = currNode.next()

        return newLL

    def filter(self, func:Callable[[Any], Any]) -> TailedLinkedList:
        '''
        Filter the Linkedlist based on a function. Returns a new TailedLinkedlist
        '''
        newLL = TailedLinkedList()
        currNode = self._LinkedList__head
        while currNode != None:
            if func(currNode.getItem()):
                newLL.addBack(currNode.getItem())
            currNode = currNode.next()

        return newLL

    def get(self, index:int) -> int:
        if index == self._LinkedList__size - 1:
            return None if self.__tail is None else self.__tail.getItem()
        return super().get(index)