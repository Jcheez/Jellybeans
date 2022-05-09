class UFDS:

    def __init__(self, sets:int) -> None:
        self.__parent = [None]
        self.__rank = [None]
        self.__assigned = {}

        for i in range(1, sets+1):
            self.__parent.append(i)
            self.__rank.append(0)
            self.__assigned[i] = set()

    def findSet(self, itemNumber: int) -> int:
        if self.__parent[itemNumber] == itemNumber:
            return itemNumber
        else:
            self.__parent[itemNumber] = self.findSet(self.__parent[itemNumber])
            return self.__parent[itemNumber]

    def isSameSet(self, firstItem:int, secondItem:int) -> bool:
        return self.findSet(firstItem) == self.findSet(secondItem)

    def union(self, firstItem:int, secondItem:int) -> None:
        if not self.isSameSet(firstItem, secondItem):
            rep_x = self.findSet(firstItem)
            rep_y = self.findSet(secondItem)

            if self.__rank[rep_x] > self.__rank[rep_y]:
                self.__parent[rep_y] = rep_x
                self.__assigned[rep_x].add(rep_y)
                union = self.__assigned[rep_x].union(self.__assigned[rep_y])
                self.__assigned[rep_x] = union
                del self.__assigned[rep_y]
            else:
                self.__parent[rep_x] = rep_y
                self.__assigned[rep_y].add(rep_x)
                union = self.__assigned[rep_y].union(self.__assigned[rep_x])
                self.__assigned[rep_y] = union
                del self.__assigned[rep_x]
                if self.__rank[rep_x] == self.__rank[rep_y]:
                    self.__rank[rep_y] += 1

    def resetSet(self, itemNumber):
        pass

    def disconnectSet(self, itemNumber):
        pass

    def countSets(self):
        pass
    