from __future__ import annotations
from .node import _Node

class _DoublyNode(_Node):
    
    def __init__(self, item, next_node=None, previous_node=None):
        self.__prev = previous_node
        super().__init__(item, next_node)

    def prev(self) -> _DoublyNode:
        return self.__prev

    def set_prev(self, new_node:_DoublyNode) -> _DoublyNode:
        self.__prev = new_node
        return self