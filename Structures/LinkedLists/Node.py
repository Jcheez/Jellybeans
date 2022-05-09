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
        self.__item = item
        self.__nextNode = nextNode

    def getItem(self) -> Any:
        return self.__item

    def next(self) -> Node:
        return self.__nextNode

    def setItem(self, newItem: Any) -> Node:
        self.__item = newItem
        return self

    def setNext(self, newNode:Node) -> Node:
        self.__nextNode = newNode
        return self