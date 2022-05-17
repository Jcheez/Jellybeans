from __future__ import annotations

class _adjPair:

    def __init__(self, vertex:int, weight:int=0) -> None:
        self.__vertex = vertex
        self.__weight = weight

    def getVertex(self) -> int:
        return self.__vertex

    def getWeight(self) -> int:
        return self.__weight

    def updateWeight(self, newWeight:int) -> _adjPair:
        self.__weight = newWeight
        return self