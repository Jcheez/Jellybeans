from __future__ import annotations
from typing import Any


class _BinaryNode:
    '''
    INTERNAL CLASS. Basic building block for constructing an AVL tree.
    '''
    def __init__(self, item) -> None:
        self.__left_node = None
        self.__right_node = None
        self.__parent = None
        self.__item = item
        self.__size = 1
        self.__height = 0

    def update_size(self) -> int:
        '''
        Updates the total number of binary nodes under this node.
        Returns:
            The updated size
        '''
        if self.__left_node == None and self.__right_node == None:
            self.__size = 1
        elif self.__left_node == None:
            self.__size = 1 + self.__right_node.get_size()
        elif self.__right_node == None:
            self.__size = 1 + self.__left_node.get_size()
        else:
            self.__size = 1 + self.__left_node.get_size() + self.__right_node.get_size()
        return self.__size

    def update_height(self) -> int:
        '''
        Updates the new height of the binary nodes under this node.
        Returns:
            The updated height
        '''
        if self.__left_node == None and self.__right_node == None:
            self.__height = 0
        elif self.__left_node == None:
            self.__height = 1 + self.__right_node.get_height()
        elif self.__right_node == None:
            self.__height = 1 + self.__left_node.get_height()
        else:
            self.__height = 1 + \
                max(self.__left_node.get_height(), self.__right_node.get_height())
        return self.__height

    def __eq__(self, other: _BinaryNode) -> bool:
        '''
        Checks if two binary nodes are equivalent.
        Returns:
            Boolean of whether the 2 objects are equal.
        '''
        if not isinstance(other, _BinaryNode):
            return False
        return self.__item == other.get_item()

    # Getters and Setters

    def get_item(self):
        return self.__item

    def get_left(self):
        return self.__left_node

    def get_right(self):
        return self.__right_node

    def get_parent(self):
        return self.__parent

    def get_size(self):
        return self.__size

    def get_height(self):
        return self.__height

    def set_left(self, new_node: _BinaryNode) -> None:
        self.__left_node = new_node

    def set_right(self, new_node: _BinaryNode) -> None:
        self.__right_node = new_node

    def set_parent(self, new_node: _BinaryNode) -> None:
        self.__parent = new_node

    def set_item(self, new_item: Any) -> None:
        self.__item = new_item
