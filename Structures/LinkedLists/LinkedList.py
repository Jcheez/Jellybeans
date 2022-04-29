from .Node import Node

class LinkedList:
    '''
    Single Linked List
    '''
    def __init__(self, item=None):
        '''
        Create a LinkedList with 0 items, i item of multiple items \n
        Args:
            item: either None, 1 item, or a list/tuple of items
        '''
        self._head = None
        self._size = 0
        if item == None:
            return
        
        if (type(item) == list or type(item) == tuple):
            for i in item:
                self.addBack(i)
        elif len(item) == 1:
            self.addBack(item)
        else:
            raise TypeError(f"Type of sequence not supported")

    def addFront(self, item):
        '''
        Adds the item to the front of the linkedList
        '''
        newNode = Node(item, self._head)
        self._head = newNode
        self._size += 1
        return self
        
    def addBack(self, item):
        '''
        Adds the item to the back of the linkedlist
        '''
        newNode = Node(item)

        if self._head == None:
            self._head = newNode
        else:
            currNode = self._head
            while currNode.next() != None:
                currNode = currNode.next()
            currNode.setNext(newNode)
        self._size += 1
        return self
    
    def addAtIndex(self, item, index):
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
            newNode = Node(item, currNode.next())
            currNode.setNext(newNode)
            self._size += 1
        return self

    def removeFront(self):
        '''
        Remove the item at the front of the linked list
        '''
        if self._size == 0:
            return self
        self._head = self._head.next()
        self._size -= 1
        return self

    def removeBack(self):
        '''
        Remove the item at the back of the linked list
        '''
        if self._size == 0:
            return self
        elif self._size == 1:
            self._head = None
            self._size -= 1
        else:
            currNode = self._head
            for iter in range(self._size - 2):
                currNode = currNode.next()
            currNode.setNext(None)
            self._size -= 1
        return self

    def removeAtIndex(self, index):
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
            self._size -= 1
            return self

    def update(self, index, newItem):
        '''
        Update the value of an item at a specified index
        Args:
            index: index to be updated
            newItem: Item to be inserted into the linkedlist
        '''
        currNode = self._head
        if currNode == None:
            return None
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index >= self._size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        
        while index > 0:
            currNode = currNode.next()
            index -= 1
        currNode.setItem(newItem)
        return self

    def get(self, index):
        '''
        Returns the item at a specified index
        '''
        currNode = self._head
        if currNode == None:
            return None
        elif index < 0:
            raise IndexError("Linkedlist does not support negative indexing")
        elif index >= self._size:
            raise IndexError("Invalid Index: Proposed index larger than size of linkedList")
        
        while index > 0:
            currNode = currNode.next()
            index -= 1
        return currNode.getItem()

    def map(self, func):
        '''
        Maps the current LinkedList to a function. Returns a new LinkedList
        '''
        newLL = LinkedList()
        currNode = self._head

        while currNode != None:
            newLL.addBack(func(currNode.getItem()))
            currNode = currNode.next()

        return newLL

    def filter(self, func):
        '''
        Filter the Linkedlist based on a function. Returns a new Linkedlist
        '''
        newLL = LinkedList()
        currNode = self._head
        while currNode != None:
            if func(currNode.getItem()):
                newLL.addBack(currNode.getItem())
            currNode = currNode.next()

        return newLL

    def to_list(self):
        '''
        Converts the LinkedList to a list
        '''
        currNode = self._head
        result = []
        while currNode != None:
            result.append(currNode.getItem())
            currNode = currNode.next()
        return result

    def __len__(self):
        '''
        Returns the size of the linkedlist
        '''
        return self._size

    def __str__(self):
        '''
        String Representation of the linkedlist
        '''
        currNode = self._head
        items = []

        if currNode == None:
            return "[]"
        
        while currNode != None:
            items.append(str(currNode.getItem()))
            currNode = currNode.next()
        return " => ".join(items)

    def __eq__(self, other):
        '''
        Tells whether two LinkedLists are equal
        '''
        if isinstance(other, LinkedList):
            return False
        elif self._size != len(other):
            return False

        curr1 = self._head
        curr2 = other._head

        while curr1 != None and curr2 != None:
            if curr1.getItem() != curr2.getItem():
                return False
            curr1 = curr1.next()
            curr2 = curr2.next()
        return True