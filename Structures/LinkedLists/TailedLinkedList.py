from .LinkedList import LinkedList
from .Node import Node

class TailedLinkedList(LinkedList):
    '''
    Tailed Linked List
    '''
    def __init__(self, items=None):
        self._tail = None
        super().__init__(items)

    def addBack(self, item):
        '''
        Adds the item to the back of the linkedlist
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

    def removeBack(self):
        '''
        Remove the item at the back of the linked list
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

    def map(self, func):
        '''
        Maps the current LinkedList to a function. Returns a new TailedLinkedList
        '''
        newLL = TailedLinkedList()
        currNode = self._head

        while currNode != None:
            newLL.addBack(func(currNode.getItem()))
            currNode = currNode.next()

        return newLL

    def filter(self, func):
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
