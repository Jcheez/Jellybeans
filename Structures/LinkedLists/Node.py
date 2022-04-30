from __future__ import annotations
from typing import Any

class Node:
    '''
    Basic Building Block of a linkedList
    Class Parameters:
        item: item to store in the node
        nextNode: Reference pointer to the next node
    '''
    def __init__(self, item:Any, nextNode:Node=None):
        self._item = item
        self._nextNode = nextNode

    def getItem(self) -> Any:
        return self._item

    def next(self) -> Node:
        return self._nextNode

    def setItem(self, newItem: Any) -> Node:
        self._item = newItem
        return self

    def setNext(self, newNode:Node) -> Node:
        self._nextNode = newNode
        return self