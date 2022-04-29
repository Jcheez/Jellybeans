class Node:
    '''
    Basic Building Block of a linkedList
    Class Parameters:
        item: item to store in the node
        nextNode: Reference pointer to the next node
    '''
    def __init__(self, item, nextNode=None):
        self._item = item
        self._nextNode = nextNode

    def getItem(self):
        return self._item

    def next(self):
        return self._nextNode

    def setItem(self, newItem):
        self._item = newItem
        return self

    def setNext(self, newNode):
        self._nextNode = newNode
        return self