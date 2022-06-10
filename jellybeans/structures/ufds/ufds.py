class UFDS:
    '''
    Union Find Disjoint Sets
    '''
    def __init__(self, sets:int) -> None:
        '''
        Args:
            Number of disjoint sets to create
        '''
        self.__parent = [None]
        self.__movements = [None]
        self.__counts = [None]
        self.__rank = [None]

        for i in range(1, sets+1):
            self.__parent.append(i)
            self.__movements.append(i)
            self.__rank.append(0)
            self.__counts.append(1)

    def find_set(self, item_number: int) -> int:
        '''
        Finds the representative node of the set containing 'item_number'

        Args:
            item_number: set number
        Returns:
            Number of representative set
        '''
        item_number = self.__movements[item_number]
        if self.__parent[item_number] == item_number:
            return item_number
        else:
            self.__parent[item_number] = self.find_set(self.__parent[item_number])
            return self.__parent[item_number]

    def is_same_set(self, first_item:int, second_item:int) -> bool:
        '''
        Checks if 2 items belong to the same set

        Args:
            first_item: First Set
            second_item: Second Set
        Returns:
            True if first_item and second_item belong to the same set
        '''
        return self.find_set(first_item) == self.find_set(second_item)

    def union(self, first_item:int, second_item:int) -> None:
        '''
        Unions 2 sets together

        Args:
            first_item: First Set
            second_item: Second Set
        '''
        if not self.is_same_set(first_item, second_item):
            rep_x = self.find_set(first_item)
            rep_y = self.find_set(second_item)

            if self.__rank[rep_x] > self.__rank[rep_y]:
                self.__parent[rep_y] = rep_x
                self.__counts[rep_x] += self.__counts[rep_y]
            else:
                self.__parent[rep_x] = rep_y
                self.__counts[rep_y] += self.__counts[rep_x]
                if self.__rank[rep_x] == self.__rank[rep_y]:
                    self.__rank[rep_y] += 1

    def move(self, item_number:int, destination_number:int) -> None:
        '''
        Move an item from its original set to a new set

        Args:
            item_number: Original set number
            destination_number: New set number
        '''
        root_from = self.find_set(self.__movements[item_number])
        root_to = self.find_set(self.__movements[destination_number])
        if (root_from != root_to):
            self.__counts[root_from] -= 1
            self.__counts[root_to] += 1
            self.__movements[item_number] = root_to

    def count_items(self, item_number: int) -> int:
        '''
        Count the number of items in a particular set

        Args:
            item_number: Set number

        Returns:
            Total number of items in that set
        '''
        rep = self.find_set(self.__movements[item_number])
        return self.__counts[rep]