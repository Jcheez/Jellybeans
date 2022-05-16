from __future__ import annotations
from .Node import _Node

class _DoublyNode(_Node):
    
    def __init__(self, item, nextNode=None, previousNode=None):
        self.__prev = previousNode
        super().__init__(item, nextNode)

    def prev(self) -> _DoublyNode:
        return self.__prev

    def setPrev(self, newNode:_DoublyNode) -> _DoublyNode:
        self.__prev = newNode
        return self