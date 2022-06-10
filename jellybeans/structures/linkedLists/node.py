from __future__ import annotations
from typing import Any

class _Node:
    '''
    Basic Building Block of a linkedList
    Class Parameters:
        item: item to store in the node
        nextNode: Reference pointer to the next node
    '''
    def __init__(self, item:Any, next_node:_Node=None):
        self.__item = item
        self.__next_node = next_node

    def get_item(self) -> Any:
        return self.__item

    def next(self) -> _Node:
        return self.__next_node

    def set_item(self, new_item: Any) -> _Node:
        self.__item = new_item
        return self

    def set_next(self, new_node:_Node) -> _Node:
        self.__next_node = new_node
        return self