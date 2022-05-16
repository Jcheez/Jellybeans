from __future__ import annotations
from typing import Any

class _Node:
    '''
    Basic Building Block of a linkedList
    Class Parameters:
        item: item to store in the node
        nextNode: Reference pointer to the next node
    '''
    def __init__(self, item:Any, nextNode:_Node=None):
        self.__item = item
        self.__nextNode = nextNode

    def getItem(self) -> Any:
        return self.__item

    def next(self) -> _Node:
        return self.__nextNode

    def setItem(self, newItem: Any) -> _Node:
        self.__item = newItem
        return self

    def setNext(self, newNode:_Node) -> _Node:
        self.__nextNode = newNode
        return self