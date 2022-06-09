from __future__ import annotations
from Jellybeans.exceptions.GraphProperty import _GraphProperty
from .pfuncs import _is_connected_n_acyclic, _topo_sort

class Graph:

    def __init__(self) -> None:
        self.__adjList = {}
        self.__reachableBy = {}
        self.__unweighted = [True, None]
        self.__positive_weighted = True

    def add_vertex(self, nodeId:int) -> None:
        if nodeId not in self.__adjList and nodeId not in self.__reachableBy:
            self.__adjList[nodeId] = []
            self.__reachableBy[nodeId] = []
        else:
            raise _GraphProperty("Vertex already present in graph")

    def delete_vertex(self, vertex:int) -> None:
        if vertex not in self.__adjList or vertex not in self.__reachableBy:
            raise _GraphProperty(f"Vertex {vertex} not present in graph")
        reachable = self.can_reach(vertex)
        connected = self.neighbours_of(vertex)

        for tex in reachable:
            self.delete_edge([tex, vertex])

        for node in connected:
            self.delete_edge([vertex, node])

        del self.__adjList[vertex]
        del self.__reachableBy[vertex]
        
    def list_vertices(self) -> list:
        return list(self.__adjList.keys())

    def num_vertices(self) -> int:
        return len(self.__adjList)

    def add_edge(self, vFrom:int, vTo:int, weight:int = 1) -> None:
        if vFrom == vTo:
            raise _GraphProperty("Edges must connect 2 different vertices together")
        if vFrom not in self.__adjList or vTo not in self.__adjList:
            raise _GraphProperty(f"Unable to add edge as vertex {vFrom} or {vTo} not present in graph")
        edges = self.__adjList[vFrom]
        for v,_ in edges:
            if v == vTo:
                raise _GraphProperty(f"Edge {vFrom} -> {vTo} already present in graph")
        edges.append((vTo, weight))
        if self.__unweighted[1] is None:
            self.__unweighted[1] = weight
        else:
            if self.__unweighted[0]:
                self.__unweighted[0] = weight == self.__unweighted[1]

        if self.__positive_weighted:
            self.__positive_weighted = weight >= 0
        self.__reachableBy[vTo].append(vFrom)
    
    def add_bidirected_edge(self, vFrom:int, vTo:int, weight:tuple = (1,1)):
        self.add_edge(vFrom, vTo, weight[0])
        self.add_edge(vTo, vFrom, weight[1])
    
    def delete_edge(self, edge:list) -> None:
        vFrom, vTo = edge

        new_adjList = []
        edge_counter = 0
        for e in self.__adjList[vFrom]:
            if e[0] != vTo:
                new_adjList.append(e)
                edge_counter += 1
        if edge_counter == len(self.__adjList[vFrom]):
            raise _GraphProperty(f"Edge {edge} not found in the graph")
        
        self.__adjList[vFrom] = new_adjList
        self.__reachableBy[vTo].remove(vFrom)

    def update_edge_weight(self, edge:list, newWeight:int) -> None:
        vFrom, vTo = edge
        self.delete_edge(edge)
        self.add_edge(vFrom, vTo, newWeight)

    def neighbours_of(self, vertex:int) -> list:
        return [x[0] for x in self.edges_of(vertex)]

    def num_neighbours(self, vertex:int) -> int:
        return len(self.neighbours_of(vertex))

    def edges_of(self, vertex:int) -> list:
        return self.__adjList[vertex].copy()

    def can_reach(self, vertex:int) -> list:
        return self.__reachableBy[vertex].copy()

    def to_edgeList(self) -> list:
        res = []
        for vertex in self.list_vertices():
            edges = self.__adjList[vertex]
            for e in edges:
                complete_edge = (vertex,) + e
                res.append(complete_edge)
        return res

    def transpose(self) -> Graph:
        newG = Graph()
        for v in self.list_vertices():
            newG.add_vertex(v)
        for vFrom, vTo, weight in self.to_edgeList():
            newG.add_edge(vTo, vFrom, -weight)
        return newG
        
    def to_adjList(self) -> dict:
        return self.__adjList.copy()

    def to_adjMatrix(self):
        vertices = self.list_vertices()
        mapping = {v:idx for idx,v in enumerate(vertices)}
        res = [[0 for _ in vertices] for _ in vertices]
    
        for v in vertices:
            for neighbor, weight in self.__adjList[v]:
                res[mapping[v]][mapping[neighbor]] = weight
        return mapping, res

    def is_tree(self) -> bool:
        vertices = self.list_vertices()
        for v in vertices:
            res = _is_connected_n_acyclic(vertices, self.__adjList, v)
            if not res:
                return False
        return True
        
    def is_unweighted(self) -> bool:
        return self.__unweighted[0]

    def is_positive(self) -> bool:
        return self.__positive_weighted

    def is_DAG(self) -> bool:

        toposort = _topo_sort(self.list_vertices(), self.to_adjList(), self.to_edgeList())
        
        if len(toposort) < len(self.__adjList):
            return False
        idxs = {toposort[idx]: idx for idx in range(len(toposort))}
        for v,edges in self.__adjList.items():
            for edge,_ in edges:
                idx_v = idxs[v]
                idx_w = idxs[edge]
                if idx_v > idx_w:
                    return False
        return True