from typing import Any

class Stack:
    '''
    Stack is a LIFO Data structure
    '''
    def __init__(self) -> None:
        self.__size = 0
        self.__stack = []

    def is_empty(self) -> bool:
        '''
        Checks if there are elements in the stack

        Returns:
            True if stack has 0 elements
        '''
        return self.__size == 0

    def peek(self) -> Any:
        '''
        Returns:
            element at the top of the stack
        '''
        if self.is_empty():
            return None
        return self.__stack[self.__size - 1]

    def pop(self) -> Any:
        '''
        Returns and remove the element at the top of the stack

        Returns:
            element at the top of the stack
        '''
        if self.is_empty():
            raise IndexError("Popping an empty stack")
        self.__size -= 1
        return self.__stack.pop()

    def push(self, item:Any) -> None:
        '''
        Insert an item into the top of the stack

        Args:
            item: Item to be inserted
        '''
        self.__stack.append(item)
        self.__size += 1

    def __len__(self) -> int:
        '''
        Returns the size of the stack
        '''
        return self.__size

    def __str__(self) -> str:
        '''
        Visual Representation of the stack
        '''
        if self.__size == 0:
            return "[]"
        result = ""
        for idx in range(len(self.__stack) - 1, -1, -1):
            result += str(self.__stack[idx])
            if idx > 0:
                result += " <- "
        return result
