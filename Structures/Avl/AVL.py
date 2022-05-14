from __future__ import annotations
from typing import Any, Callable

from soupsieve import select
from .binaryNode import binaryNode

class AVL:
    '''
    This data structure represents a self balancing binary tree
    '''
    def __init__(self, comparator:Callable = lambda x,y: x>=y) -> None:
        '''
        Comparators should be defined in the following format: \n
        (x, y) => x>=y
        '''
        self.__root = None
        self.comparator = comparator

    def __helper_search(self, currNode: binaryNode, item) -> binaryNode:
        if currNode is None:
            return None
        elif currNode.getItem() == item:
            return currNode
        elif self.comparator(currNode.getItem(), item):
            return self.__helper_search(currNode.getLeft(), item)
        else:
            return self.__helper_search(currNode.getRight(), item)
        
    def search(self, item:Any) -> bool:
        res = self.__helper_search(self.__root, item)
        return None if res is None else res.getItem()

    def insert(self, item:Any) -> None:
        
        def helper(currNode:binaryNode, item:Any) -> binaryNode:
            if currNode is None:
                return binaryNode(item)
            elif self.comparator(currNode.getItem(), item):
                currNode.setLeft(helper(currNode.getLeft(), item))
                currNode.getLeft().setParent(currNode)
            else:
                currNode.setRight(helper(currNode.getRight(), item))
                currNode.getRight().setParent(currNode)

            if currNode is not None:
                currNode.updateHeight()
                currNode.updateSize()

            return currNode

        self.__root = helper(self.__root, item)
                
    def delete(self, item:Any) -> None:
        
        def helper_delete(currNode:binaryNode, item:Any) -> binaryNode:
            if currNode is None:
                return currNode
            elif currNode.getItem() == item:
                if currNode.getLeft() is None and currNode.getRight() is None:
                    currNode = None
                elif currNode.getLeft() is None:
                    currNode.getRight().setParent(currNode.getParent())
                    currNode = currNode.getRight()
                elif currNode.getRight() is None:
                    currNode.getLeft().setParent(currNode.getParent())
                    currNode = currNode.getLeft()
                else:
                    item_successor = self.successor(item)
                    currNode.setItem(item_successor)
                    currNode.setRight(helper_delete(currNode.getRight(), item_successor))
            elif self.comparator(currNode.getItem(), item):
                currNode.setLeft(helper_delete(currNode.getLeft(), item))
            else:
                currNode.setRight(helper_delete(currNode.getRight(), item))

                currNode.updateHeight()
                currNode.updateSize()

            return currNode

        self.__root = helper_delete(self.__root, item)

    def min(self) -> Any:
        currNode = self.__root
        while currNode.getLeft() is not None:
            currNode = currNode.getLeft()
        return currNode.getItem()

    def max(self) -> Any:
        currNode = self.__root
        while currNode.getRight() is not None:
            currNode = currNode.getRight()
        return currNode.getItem()

    def successor(self, item:Any) -> Any:
        
        def successor_helper(currNode:binaryNode) -> binaryNode:
            if currNode.getRight() is not None:
                tempNode = currNode.getRight()
                while tempNode.getLeft() is not None:
                    currNode = currNode.getLeft()
                return tempNode
            else:
                curr = currNode
                parent = currNode.getParent()
                while parent is not None and curr == parent.getRight():
                    curr = parent
                    parent = parent.getParent()
                return parent

        target = self.__helper_search(self.__root, item)
        res = successor_helper(target)
        return None if res is None else res.getItem()

    def predecessor(self, item:Any) -> Any:
        
        def predecessor_helper(currNode:binaryNode) -> binaryNode:
            if currNode.getLeft() is not None:
                tempNode = currNode.getLeft()
                while tempNode.getRight() is not None:
                    currNode = currNode.getRight()
                return tempNode
            else:
                curr = currNode
                parent = currNode.getParent()
                while parent is not None and curr == parent.getLeft():
                    curr = parent
                    parent = parent.getParent()
                return parent

        target = self.__helper_search(self.__root, item)
        res = predecessor_helper(target)
        return None if res is None else res.getItem()

    def rank(self, item:Any) -> int:
        
        def rank_helper(currNode:binaryNode, item:Any) -> int:
            if currNode == None:
                return 0
            if currNode.getItem() == item:
                return currNode.getLeft().getSize() + 1 if currNode.getLeft() is not None else 1
            elif self.comparator(currNode.getItem(), item):
                return rank_helper(currNode.getLeft(), item)
            else:
                res = currNode.getLeft().getSize() + 1 if currNode.getLeft() is not None else 1
                res += rank_helper(currNode.getRight(), item)
                return res
        
        return rank_helper(self.__root, item)

    def select(self, rank:int) -> Any:
        
        def select_helper(currNode:binaryNode, rank:int) -> binaryNode:
            leftSize = currNode.getLeft().getSize() + 1 if currNode.getLeft() is not None else 1
            if currNode is None:
                return None
            if leftSize == rank:
                return currNode
            elif leftSize > rank:
                return select_helper(currNode.getLeft(), rank)
            else:
                return select_helper(currNode.getRight(), rank - leftSize)

        res = select_helper(self.__root, rank)

        return res.getItem() if res is not None else None

    def print(self, type:int = 1) -> None:
        
        def in_order_helper(currNode):
            if currNode == None:
                return
            in_order_helper(currNode.getLeft())
            print(currNode.getItem(), end= " ")
            in_order_helper(currNode.getRight())
        
        def pre_order_helper(currNode):
            if currNode == None:
                return
            print(currNode.getItem(), end= " ")
            pre_order_helper(currNode.getLeft())
            pre_order_helper(currNode.getRight())

        def post_order_helper(currNode):
            if currNode == None:
                return
            post_order_helper(currNode.getLeft())
            post_order_helper(currNode.getRight())
            print(currNode.getItem(), end= " ")
        
        if type == 1:
            in_order_helper(self.__root)
        elif type == 2:
            pre_order_helper(self.__root)
        elif type == 3:
            post_order_helper(self.__root)