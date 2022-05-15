from __future__ import annotations
from typing import Any


class binaryNode:

    def __init__(self, item) -> None:
        self.__leftNode = None
        self.__rightNode = None
        self.__parent = None
        self.__item = item
        self.__size = 1
        self.__height = 0

    def updateSize(self) -> int:
        if self.__leftNode == None and self.__rightNode == None:
            self.__size = 1
        elif self.__leftNode == None:
            self.__size = 1 + self.__rightNode.getSize()
        elif self.__rightNode == None:
            self.__size = 1 + self.__leftNode.getSize()
        else:
            self.__size = 1 + self.__leftNode.getSize() + self.__rightNode.getSize()
        return self.__size

    def updateHeight(self) -> int:
        if self.__leftNode == None and self.__rightNode == None:
            self.__height = 0
        elif self.__leftNode == None:
            self.__height = 1 + self.__rightNode.getHeight()
        elif self.__rightNode == None:
            self.__height = 1 + self.__leftNode.getHeight()
        else:
            self.__height = 1 + \
                max(self.__leftNode.getHeight(), self.__rightNode.getHeight())
        return self.__height

    def __eq__(self, other: binaryNode) -> bool:
        if not isinstance(other, binaryNode):
            return False
        return self.__item == other.getItem()

    def getItem(self):
        return self.__item

    def getLeft(self):
        return self.__leftNode

    def getRight(self):
        return self.__rightNode

    def getParent(self):
        return self.__parent

    def getSize(self):
        return self.__size

    def getHeight(self):
        return self.__height

    def setLeft(self, newNode: binaryNode) -> None:
        self.__leftNode = newNode

    def setRight(self, newNode: binaryNode) -> None:
        self.__rightNode = newNode

    def setParent(self, newNode: binaryNode) -> None:
        self.__parent = newNode

    def setItem(self, newItem: Any) -> None:
        self.__item = newItem
