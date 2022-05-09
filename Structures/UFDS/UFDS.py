class UFDS:
    '''
    Union Find Disjoint Sets
    '''
    def __init__(self, sets:int) -> None:
        # MOVEMENTS AND COUNTS HAVE NOT BEEN IMPLEMENTED
        self.__parent = [None]
        self.__movements = [None]
        self.__counts = [None]
        self.__rank = [None]

        for i in range(1, sets+1):
            self.__parent.append(i)
            self.__movements.append(i)
            self.__rank.append(0)
            self.__counts.append(0)

    def findSet(self, itemNumber: int) -> int:
        '''
        Finds the representative node of the set containing 'itemNumber'
        '''
        if self.__parent[itemNumber] == itemNumber:
            return itemNumber
        else:
            self.__parent[itemNumber] = self.findSet(self.__parent[itemNumber])
            return self.__parent[itemNumber]

    def isSameSet(self, firstItem:int, secondItem:int) -> bool:
        '''
        Checks if 2 items belong to the same set
        '''
        return self.findSet(firstItem) == self.findSet(secondItem)

    def union(self, firstItem:int, secondItem:int) -> None:
        '''
        Unions 2 sets together
        '''
        if not self.isSameSet(firstItem, secondItem):
            rep_x = self.findSet(firstItem)
            rep_y = self.findSet(secondItem)

            if self.__rank[rep_x] > self.__rank[rep_y]:
                self.__parent[rep_y] = rep_x
            else:
                self.__parent[rep_x] = rep_y
                if self.__rank[rep_x] == self.__rank[rep_y]:
                    self.__rank[rep_y] += 1

    def move(self, itemNumber, destinationNumber):
        '''
        Move an item from its original set to a new set
        '''
        pass

    def countItems(self, itemNumber) -> int:
        '''
        Count the number of items in a particular set
        '''
        pass
    