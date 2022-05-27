from __future__ import annotations
from Jellybeans.Structures import Queue
from Jellybeans.Exceptions.GraphProperty import _GraphProperty
from .pfuncs import _DFS_tree

class Graph:

    def __init__(self) -> None:
        self.__adjList = {}
        self.__reachableBy = {}
        self.__unweighted = True
        self.__first_weight = None

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
        if self.__first_weight is None:
            self.__first_weight = weight
        else:
            self.__unweighted = False if weight != self.__first_weight else True
        self.__reachableBy[vTo].append(vFrom)
    
    def add_bidirected_edge(self, vFrom:int, vTo:int, weight:tuple):
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
        return self.__adjList

    def to_adjMatrix(self):
        vertices = self.list_vertices()
        res = []
        mapping = {}
        # find out the number of vertices
        counter = 0
        for v in vertices:
            row = [0 for x in vertices]
            res.append(row)
            mapping[v] = counter
            counter += 1
        # fill the x*x matrix first with 0 values
        for vFrom in vertices:
            lst = self.__adjList[vFrom]
            for vTo,weight in lst:
                res[mapping[vFrom]][mapping[vTo]] = weight
        return mapping, res

    def is_tree(self) -> bool:
        visited = []
        parent = []
        mapping = {}
        counter = 0
        vertices = self.list_vertices()
        for v in vertices:
            visited.append(0)
            parent.append(-1)
            mapping[v] = counter
            counter += 1
        parent[0] = 0
        if not _DFS_tree(visited, vertices[0], self.__adjList, mapping, parent):
            return False
        for visit in visited:
            if visit == 0:
                return False
        return True

    def is_unweighted(self) -> bool:
        return self.__unweighted

    def is_DAG(self) -> bool:
       
        def topo_sort(graph:Graph) -> list:
            '''
            Performs a topological sort on the graph. Based on Kahn's Algorithm \n
            Args:
                graph: Graph object
            Returns:
                List containing a valid topological ordering
            '''
            in_degree = []
            mapping = {}
            toposort = []
            vertices = graph.list_vertices()
            inv_map = [0 for _ in vertices]
            adj_list = graph.to_adjList()
            counter = 0
            q = Queue()
            for v in vertices:
                in_degree.append(0)
                mapping[v] = counter
                inv_map[counter] = v
                counter += 1
            for _, vTo,_ in graph.to_edgeList():
                in_degree[mapping[vTo]] += 1

            for idx in range(len(in_degree)):
                if in_degree[idx] == 0:
                    q.enqueue(inv_map[idx])

            while not q.isEmpty():
                tex = q.dequeue()
                toposort.append(tex)
                for v,_ in adj_list[tex]:
                    in_degree[mapping[v]] -= 1
                    if in_degree[mapping[v]] == 0:
                        q.enqueue(v)
            return toposort

        toposort = topo_sort(self)
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