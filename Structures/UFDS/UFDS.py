class UFDS:

    def __init__(self, sets:int) -> None:
        self._sets = sets
        self._parent = [None]
        self._rank = [None]

        for i in range(1, sets+1):
            self._parent.append(i)
            self._rank.append(0)

    def findSet(self, itemNumber: int) -> int:
        if self._parent[itemNumber] == itemNumber:
            return itemNumber
        else:
            self._parent[itemNumber] = self.findSet(self._parent[itemNumber])
            return self._parent[itemNumber]

    def isSameSet(self, firstItem:int, secondItem:int) -> bool:
        return self.findSet(firstItem) == self.findSet(secondItem)

    def union(self, firstItem:int, secondItem:int) -> None:
        pass

    def resetSet(self, itemNumber):
        pass

    def disconnectSet(self, itemNumber):
        pass

    def countSets(self):
        pass
    