from Jellybeans.Exceptions.GraphProperty import _GraphProperty

class Graph:

    def __init__(self) -> None:
        self.__adjList = {}
        self.__reachableBy = {}

    def add_vertex(self, nodeId:int) -> None:
        if nodeId not in self.__adjList and nodeId not in self.__reachableBy:
            self.__adjList[nodeId] = []
            self.__reachableBy[nodeId] = []
        else:
            raise _GraphProperty("Vertex already present in graph")

    def delete_vertex(self, vertex:int) -> None:
        # Get nodes that point to vertex from reachableBy
        if vertex not in self.__adjList or vertex not in self.__reachableBy:
            raise _GraphProperty(f"Vertex {vertex} not present in graph")
        reachable = self.can_reach(vertex)
        connected = self.neighbours_of(vertex)
        # Delete the corresponding edges from self.__adjList
        for tex in reachable:
            self.delete_edge([tex, vertex])
        for node in connected:
            self.delete_edge([vertex, node])
        # delete node from adjList and from reachableBy
        del self.__adjList[vertex]
        del self.__reachableBy[vertex]
        
    def list_vertices(self) -> list:
        return list(self.__adjList.keys())

    def num_vertices(self) -> int:
        return len(self.list_vertices())

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
        self.__reachableBy[vTo].append(vFrom)
    
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

    def neighbours_of(self, vertex:int) -> list:
        return [x[0] for x in self.edges_of(vertex)]

    def num_neighbours(self, vertex:int) -> int:
        return len(self.neighbours_of(vertex))

    def edges_of(self, vertex:int) -> list:
        return self.__adjList[vertex]

    def can_reach(self, vertex:int) -> list:
        return self.__reachableBy[vertex]

    def to_edgeList(self):
        pass

    def to_adjList(self):
        pass

    def to_adjMatrix(self):
        pass