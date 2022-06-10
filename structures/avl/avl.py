from __future__ import annotations
from typing import Any, Callable
from .binary_node import _BinaryNode


class Avl:
    '''
    This data structure represents a self balancing binary tree
    '''

    def __init__(self, comparator: Callable = lambda x, y: x >= y) -> None:
        '''
        Args:
            comparator: Function which is used to decide the relative ordering of elements
        Comparators should be defined in the following format: 

        (x, y) => x>=y
        '''
        self.__root = None
        self.comparator = comparator

    def __helper_search(self, curr_node: _BinaryNode, item) -> _BinaryNode:
        '''
        INTERNAL FUNCTION: Helper function to find a particular item in the tree 

        Args:
            curr_node: The current Node to perform the search on
            item: The item that is to be found
        Returns:
            None or The Node which contains the item
        '''
        if curr_node is None:
            return None
        elif curr_node.get_item() == item:
            return curr_node
        elif self.comparator(curr_node.get_item(), item):
            return self.__helper_search(curr_node.get_left(), item)
        else:
            return self.__helper_search(curr_node.get_right(), item)

    def __balance_factor(self, curr_node: _BinaryNode) -> int:
        '''
        INTERNAL FUNCTION: Function to find the balance factor of a particular node 

        Args:
            curr_node: The node to get the balance factor
        Returns:
            The balance factor
        '''
        left = -1 if curr_node.get_left() is None else curr_node.get_left().get_height()
        right = -1 if curr_node.get_right() is None else curr_node.get_right().get_height()
        return left - right

    def __rotate_left(self, curr_node: _BinaryNode) -> _BinaryNode:
        '''
        INTERNAL FUNCTION: Perform a left rotation about the current node 

        Args:
            curr_node: The node to perform a left rotation
        Returns:
            The new pivot node
        '''
        rc = curr_node.get_right()
        if rc is None:
            return None
        rc.set_parent(curr_node.get_parent())
        if rc.get_parent() is None:
            self.__root = rc
        curr_node.set_parent(rc)
        curr_node.set_right(rc.get_left())
        if rc.get_left() is not None:
            rc.get_left().set_parent(curr_node)
        rc.set_left(curr_node)
        curr_node.update_size()
        curr_node.update_height()
        rc.update_size()
        rc.update_height()
        return rc

    def __rotate_right(self, curr_node: _BinaryNode) -> _BinaryNode:
        '''
        INTERNAL FUNCTION: Perform a right rotation about the current node 

        Args:
            curr_node: The node to perform a right rotation
        Returns:
            The new pivot node
        '''
        lc = curr_node.get_left()
        if lc is None:
            return None
        lc.set_parent(curr_node.get_parent())
        if lc.get_parent() is None:
            self.__root = lc
        curr_node.set_parent(lc)
        curr_node.set_left(lc.get_right())
        if lc.get_right() is not None:
            lc.get_right().set_parent(curr_node)
        lc.set_right(curr_node)
        curr_node.update_size()
        curr_node.update_height()
        lc.update_size()
        lc.update_height()
        return lc

    def __balance(self, curr_node: _BinaryNode) -> _BinaryNode:
        '''
        INTERNAL FUNCTION: Checks for inbalance at a node and performs the necessary rotations 

        Args:
            curr_node: The node to balance
        Returns:
            The new pivot
        '''
        factor = self.__balance_factor(curr_node)
        if factor == 2:
            if self.__balance_factor(curr_node.get_left()) == -1:
                curr_node.setLeft(self.__rotate_left(curr_node.get_left()))
                curr_node = self.__rotate_right(curr_node)
            else:
                curr_node = self.__rotate_right(curr_node)
        elif factor == -2:
            if self.__balance_factor(curr_node.get_right()) == 1:
                curr_node.set_right(self.__rotate_right(curr_node.get_right()))
                curr_node = self.__rotate_left(curr_node)
            else:
                curr_node = self.__rotate_left(curr_node)

        return curr_node

    def search(self, item: Any) -> Any:
        '''
        Search for an item in the tree 

        Args:
            item: The item to search for
        Returns:
            None or item
        '''
        res = self.__helper_search(self.__root, item)
        return None if res is None else res.get_item()

    def insert(self, item: Any) -> None:
        '''
        Insert an element into the tree 

        Args:
            item: The item to be inserted into the tree
        '''
        def helper(curr_node: _BinaryNode, item: Any) -> _BinaryNode:
            if curr_node is None:
                return _BinaryNode(item)
            elif self.comparator(curr_node.get_item(), item):
                curr_node.set_left(helper(curr_node.get_left(), item))
                curr_node.get_left().set_parent(curr_node)
            else:
                curr_node.set_right(helper(curr_node.get_right(), item))
                curr_node.get_right().set_parent(curr_node)

            if curr_node is not None:
                curr_node.update_height()
                curr_node.update_size()
                curr_node = self.__balance(curr_node)

            return curr_node

        self.__root = helper(self.__root, item)

    def delete(self, item: Any) -> None:
        '''
        Delete an element from the tree 

        Args:
            item: The item to be deleted from the tree
        '''
        def helper_delete(curr_node: _BinaryNode, item: Any) -> _BinaryNode:
            if curr_node is None:
                return curr_node
            elif curr_node.get_item() == item:
                if curr_node.get_left() is None and curr_node.get_right() is None:
                    curr_node = None
                elif curr_node.get_left() is None:
                    curr_node.get_right().set_parent(curr_node.get_parent())
                    curr_node = curr_node.get_right()
                elif curr_node.get_right() is None:
                    curr_node.get_left().set_parent(curr_node.get_parent())
                    curr_node = curr_node.get_left()
                else:
                    item_successor = self.successor(item)
                    curr_node.set_item(item_successor)
                    curr_node.set_right(helper_delete(
                        curr_node.get_right(), item_successor))
            elif self.comparator(curr_node.get_item(), item):
                curr_node.set_left(helper_delete(curr_node.get_left(), item))
            else:
                curr_node.set_right(helper_delete(curr_node.get_right(), item))

            if curr_node is not None:
                curr_node.update_height()
                curr_node.update_size()
                curr_node = self.__balance(curr_node)

            return curr_node

        self.__root = helper_delete(self.__root, item)

    def min(self) -> Any:
        '''
        Find the smallest element in the tree 

        Returns:
            The item which is the minimum
        '''
        curr_node = self.__root
        while curr_node.get_left() is not None:
            curr_node = curr_node.get_left()
        return curr_node.get_item()

    def max(self) -> Any:
        '''
        Find the largest element in the tree 

        Returns:
            The item which is the maximum
        '''
        curr_node = self.__root
        while curr_node.get_right() is not None:
            curr_node = curr_node.get_right()
        return curr_node.get_item()

    def successor(self, item: Any) -> Any:
        '''
        Finds the next biggest element after "item" 

        Args:
            item: To find the successor of this item
        Returns:
            The successor of the item
        '''
        def successor_helper(curr_node: _BinaryNode) -> _BinaryNode:
            if curr_node.get_right() is not None:
                temp_node = curr_node.get_right()
                while temp_node.get_left() is not None:
                    curr_node = curr_node.get_left()
                return temp_node
            else:
                curr = curr_node
                parent = curr_node.get_parent()
                while parent is not None and curr == parent.get_right():
                    curr = parent
                    parent = parent.get_parent()
                return parent

        target = self.__helper_search(self.__root, item)
        res = successor_helper(target)
        return None if res is None else res.get_item()

    def predecessor(self, item: Any) -> Any:
        '''
        Finds the next smallest element after "item" 

        Args:
            item: To find the predecessor of this item
        Returns:
            The predecessor of the item
        '''
        def predecessor_helper(curr_node: _BinaryNode) -> _BinaryNode:
            if curr_node.get_left() is not None:
                temp_node = curr_node.get_left()
                while temp_node.get_right() is not None:
                    curr_node = curr_node.get_right()
                return temp_node
            else:
                curr = curr_node
                parent = curr_node.get_parent()
                while parent is not None and curr == parent.get_left():
                    curr = parent
                    parent = parent.get_parent()
                return parent

        target = self.__helper_search(self.__root, item)
        res = predecessor_helper(target)
        return None if res is None else res.get_item()

    def rank(self, item: Any) -> int:
        '''
        Finds the rank of a particular item 

        Args:
            item: To find the rank of this item
        Returns:
            The item's rank
        '''
        def rank_helper(curr_node: _BinaryNode, item: Any) -> int:
            if curr_node == None:
                return -1
            if curr_node.get_item() == item:
                return curr_node.get_left().get_size() + 1 if curr_node.get_left() is not None else 1
            elif self.comparator(curr_node.get_item(), item):
                return rank_helper(curr_node.get_left(), item)
            else:
                left = curr_node.get_left().get_size() + 1 if curr_node.get_left() is not None else 1
                right = rank_helper(curr_node.get_right(), item)
                res = -1 if right == -1 else left + right
                return res

        return rank_helper(self.__root, item)

    def select(self, rank: int) -> Any:
        '''
        Given the rank, find the associated item 

        Args:
            rank: The rank of the item
        Returns:
            The item
        '''
        def select_helper(curr_node: _BinaryNode, rank: int) -> _BinaryNode:
            if curr_node is None:
                return None
            left_size = curr_node.get_left().get_size() + 1 if curr_node.get_left() is not None else 1
            if left_size == rank:
                return curr_node
            elif left_size > rank:
                return select_helper(curr_node.get_left(), rank)
            else:
                return select_helper(curr_node.get_right(), rank - left_size)

        res = select_helper(self.__root, rank)

        return res.get_item() if res is not None else None

    def in_order(self) -> list:
        '''
        Conduct an in order traversal of the tree and output the result in a list 

        Returns:
            list of in order sequence
        '''
        def in_order_helper(curr_node: _BinaryNode) -> list:
            if curr_node == None:
                return []
            return in_order_helper(curr_node.get_left()) + [curr_node.get_item()] + in_order_helper(curr_node.get_right())

        return in_order_helper(self.__root)

    def pre_order(self) -> list:
        '''
        Conduct a pre order traversal of the tree and output the result in a list 

        Returns:
            list of pre order sequence
        '''
        def pre_order_helper(curr_node: _BinaryNode) -> list:
            if curr_node == None:
                return []
            return [curr_node.get_item()] + pre_order_helper(curr_node.get_left()) + pre_order_helper(curr_node.get_right())

        return pre_order_helper(self.__root)

    def post_order(self) -> list:
        '''
        Conduct a post order traversal of the tree and output the result in a list 

        Returns:
            list of post order sequence
        '''
        def post_order_helper(curr_node: _BinaryNode) -> list:
            if curr_node == None:
                return []
            return post_order_helper(curr_node.get_left()) + post_order_helper(curr_node.get_right()) + [curr_node.get_item()]

        return post_order_helper(self.__root)

    def print(self, type: int = 1) -> None:
        '''
        3 Types of prints available: 

        In order Traversal (type = 1) 

        Pre order Traversal (type = 2) 

        Post order Traversal (type = 3) 


        Args:
            type: see above
        '''
        if type == 1:
            print(self.in_order())
        elif type == 2:
            print(self.pre_order())
        elif type == 3:
            print(self.post_order())
