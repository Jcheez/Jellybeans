from __future__ import annotations
from .Node import Node

class DoublyNode(Node):
    
    def __init__(self, item, nextNode=None, previousNode=None):
        self.__prev = previousNode
        super().__init__(item, nextNode)

    def prev(self) -> DoublyNode:
        return self.__prev

    def setPrev(self, newNode:DoublyNode) -> DoublyNode:
        self.__prev = newNode
        return self