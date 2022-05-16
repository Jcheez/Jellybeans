from __future__ import annotations
from typing import Any, Callable
from .binaryNode import _binaryNode


class AVL:
    '''
    This data structure represents a self balancing binary tree
    '''

    def __init__(self, comparator: Callable = lambda x, y: x >= y) -> None:
        '''
        Comparators should be defined in the following format: \n
        (x, y) => x>=y
        '''
        self.__root = None
        self.comparator = comparator

    def __helper_search(self, currNode: _binaryNode, item) -> _binaryNode:
        '''
        INTERNAL FUNCTION: Helper function to find a particular item in the tree
        '''
        if currNode is None:
            return None
        elif currNode.getItem() == item:
            return currNode
        elif self.comparator(currNode.getItem(), item):
            return self.__helper_search(currNode.getLeft(), item)
        else:
            return self.__helper_search(currNode.getRight(), item)

    def __balanceFactor(self, currNode: _binaryNode) -> int:
        '''
        INTERNAL FUNCTION: Function to find the balance factor of a particular node
        '''
        left = -1 if currNode.getLeft() is None else currNode.getLeft().getHeight()
        right = -1 if currNode.getRight() is None else currNode.getRight().getHeight()
        return left - right

    def __rotateLeft(self, currNode: _binaryNode) -> _binaryNode:
        '''
        INTERNAL FUNCTION: Perform a left rotation about the current node
        '''
        rc = currNode.getRight()
        if rc is None:
            return None
        rc.setParent(currNode.getParent())
        if rc.getParent() is None:
            self.__root = rc
        currNode.setParent(rc)
        currNode.setRight(rc.getLeft())
        if rc.getLeft() is not None:
            rc.getLeft().setParent(currNode)
        rc.setLeft(currNode)
        currNode.updateSize()
        currNode.updateHeight()
        rc.updateSize()
        rc.updateHeight()
        return rc

    def __rotateRight(self, currNode: _binaryNode) -> _binaryNode:
        '''
        INTERNAL FUNCTION: Perform a right rotation about the current node
        '''
        lc = currNode.getLeft()
        if lc is None:
            return None
        lc.setParent(currNode.getParent())
        if lc.getParent() is None:
            self.__root = lc
        currNode.setParent(lc)
        currNode.setLeft(lc.getRight())
        if lc.getRight() is not None:
            lc.getRight().setParent(currNode)
        lc.setRight(currNode)
        currNode.updateSize()
        currNode.updateHeight()
        lc.updateSize()
        lc.updateHeight()
        return lc

    def __balance(self, currNode: _binaryNode) -> _binaryNode:
        '''
        INTERNAL FUNCTION: Checks for inbalance at a node and performs
        the necessary rotations 
        '''
        factor = self.__balanceFactor(currNode)
        if factor == 2:
            if self.__balanceFactor(currNode.getLeft()) == -1:
                currNode.setLeft(self.__rotateLeft(currNode.getLeft()))
                currNode = self.__rotateRight(currNode)
            else:
                currNode = self.__rotateRight(currNode)
        elif factor == -2:
            if self.__balanceFactor(currNode.getRight()) == 1:
                currNode.setRight(self.__rotateRight(currNode.getRight()))
                currNode = self.__rotateLeft(currNode)
            else:
                currNode = self.__rotateLeft(currNode)

        return currNode

    def search(self, item: Any) -> Any:
        '''
        Search for an item in the tree
        '''
        res = self.__helper_search(self.__root, item)
        return None if res is None else res.getItem()

    def insert(self, item: Any) -> None:
        '''
        Insert an element into the tree
        '''
        def helper(currNode: _binaryNode, item: Any) -> _binaryNode:
            if currNode is None:
                return _binaryNode(item)
            elif self.comparator(currNode.getItem(), item):
                currNode.setLeft(helper(currNode.getLeft(), item))
                currNode.getLeft().setParent(currNode)
            else:
                currNode.setRight(helper(currNode.getRight(), item))
                currNode.getRight().setParent(currNode)

            if currNode is not None:
                currNode.updateHeight()
                currNode.updateSize()
                currNode = self.__balance(currNode)

            return currNode

        self.__root = helper(self.__root, item)

    def delete(self, item: Any) -> None:
        '''
        Delete an element from the tree
        '''
        def helper_delete(currNode: _binaryNode, item: Any) -> _binaryNode:
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
                    currNode.setRight(helper_delete(
                        currNode.getRight(), item_successor))
            elif self.comparator(currNode.getItem(), item):
                currNode.setLeft(helper_delete(currNode.getLeft(), item))
            else:
                currNode.setRight(helper_delete(currNode.getRight(), item))

            if currNode is not None:
                currNode.updateHeight()
                currNode.updateSize()
                currNode = self.__balance(currNode)

            return currNode

        self.__root = helper_delete(self.__root, item)

    def min(self) -> Any:
        '''
        Find the smallest element in the tree
        '''
        currNode = self.__root
        while currNode.getLeft() is not None:
            currNode = currNode.getLeft()
        return currNode.getItem()

    def max(self) -> Any:
        '''
        Find the largest element in the tree
        '''
        currNode = self.__root
        while currNode.getRight() is not None:
            currNode = currNode.getRight()
        return currNode.getItem()

    def successor(self, item: Any) -> Any:
        '''
        Finds the next biggest element after "item"
        '''
        def successor_helper(currNode: _binaryNode) -> _binaryNode:
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

    def predecessor(self, item: Any) -> Any:
        '''
        Finds the next smallest element after "item"
        '''
        def predecessor_helper(currNode: _binaryNode) -> _binaryNode:
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

    def rank(self, item: Any) -> int:
        '''
        Finds the rank of a particular item
        '''
        def rank_helper(currNode: _binaryNode, item: Any) -> int:
            if currNode == None:
                return -1
            if currNode.getItem() == item:
                return currNode.getLeft().getSize() + 1 if currNode.getLeft() is not None else 1
            elif self.comparator(currNode.getItem(), item):
                return rank_helper(currNode.getLeft(), item)
            else:
                left = currNode.getLeft().getSize() + 1 if currNode.getLeft() is not None else 1
                right = rank_helper(currNode.getRight(), item)
                res = -1 if right == -1 else left + right
                return res

        return rank_helper(self.__root, item)

    def select(self, rank: int) -> Any:
        '''
        Given the rank, find the associated item
        '''
        def select_helper(currNode: _binaryNode, rank: int) -> _binaryNode:
            if currNode is None:
                return None
            leftSize = currNode.getLeft().getSize() + 1 if currNode.getLeft() is not None else 1
            if leftSize == rank:
                return currNode
            elif leftSize > rank:
                return select_helper(currNode.getLeft(), rank)
            else:
                return select_helper(currNode.getRight(), rank - leftSize)

        res = select_helper(self.__root, rank)

        return res.getItem() if res is not None else None

    def in_order(self) -> list:
        '''
        Conduct an in order traversal of the tree and output the result in a list
        '''
        def in_order_helper(currNode: _binaryNode) -> list:
            if currNode == None:
                return []
            return in_order_helper(currNode.getLeft()) + [currNode.getItem()] + in_order_helper(currNode.getRight())

        return in_order_helper(self.__root)

    def pre_order(self) -> list:
        '''
        Conduct a pre order traversal of the tree and output the result in a list
        '''
        def pre_order_helper(currNode: _binaryNode) -> list:
            if currNode == None:
                return []
            return [currNode.getItem()] + pre_order_helper(currNode.getLeft()) + pre_order_helper(currNode.getRight())

        return pre_order_helper(self.__root)

    def post_order(self) -> list:
        '''
        Conduct a post order traversal of the tree and output the result in a list
        '''
        def post_order_helper(currNode: _binaryNode) -> list:
            if currNode == None:
                return []
            return post_order_helper(currNode.getLeft()) + post_order_helper(currNode.getRight()) + [currNode.getItem()]

        return post_order_helper(self.__root)

    def print(self, type: int = 1) -> None:
        '''
        3 Types of prints available: \n
        In order Traversal (type = 1) \n
        Pre order Traversal (type = 2) \n
        Post order Traversal (type = 3) \n
        '''
        if type == 1:
            print(self.in_order())
        elif type == 2:
            print(self.pre_order())
        elif type == 3:
            print(self.post_order())
