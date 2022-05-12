from typing import Any, Callable

class AVL:
    '''
    This data structure represents a self balancing binary tree
    '''
    def __init__(self, comparator:Callable = lambda x,y: x>=y) -> None:
        self.root = None
        self.comparator = comparator

    def search(self, item: Any) -> Any:
        pass

    def insert(self, item: Any) -> None:
        pass

    def delete(self, item: Any) -> Any:
        pass

    def min(self) -> Any:
        pass

    def max(self) -> Any:
        pass

    def successor(self) -> Any:
        pass

    def predecessor(self) -> Any:
        pass

    def rank(self, item:Any) -> int:
        pass

    def select(self, rank:int) -> Any:
        pass

    def print(type:int = 1) -> None:
        pass