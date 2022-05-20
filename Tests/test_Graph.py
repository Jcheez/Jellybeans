import unittest
from Jellybeans.Structures import Graph
from Jellybeans.Exceptions.GraphProperty import _GraphProperty

class test_Graph(unittest.TestCase):
    
    def test_add_replicated_node(self):
        g = Graph()
        g.add_vertex(1)
        with self.assertRaises(_GraphProperty):
            g.add_vertex(1)

    def test_add_unreplicated_node(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        self.assertEqual(g.num_vertices(), 3)
        self.assertEqual(g.list_vertices(), [1,2,3])

    def test_add_edge_with_missing_node(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        with self.assertRaises(_GraphProperty):
            g.add_edge(1, 4, weight=3)
        with self.assertRaises(_GraphProperty):
            g.add_edge(vFrom=5, vTo=6, weight=10)

    def test_add_replicated_edge(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_edge(1, 2, weight=3)
        with self.assertRaises(_GraphProperty):
            g.add_edge(1, 2, weight=3)
        with self.assertRaises(_GraphProperty):
            g.add_edge(vFrom=1, vTo=2, weight=4)

    def test_add_edge_with_replicated_node(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        with self.assertRaises(_GraphProperty):
            g.add_edge(1,1)

    def test_add_unreplicated_edge(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(1, 3, 6)
        self.assertEqual(g.edges_of(1), [(2, 5), (3, 6)])

    def test_neighbours(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(1, 3, 6)
        self.assertEqual(g.neighbours_of(1), [2, 3])
        self.assertEqual(g.neighbours_of(2), [])

    def test_neighbours_length(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(1, 3, 6)
        self.assertEqual(g.num_neighbours(1), 2)
        self.assertEqual(g.num_neighbours(2), 0)

    def test_reachability(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(3, 2, 6)
        self.assertEqual(g.can_reach(2), [1,3])
        self.assertEqual(g.can_reach(1), [])
        self.assertEqual(g.can_reach(3), [])

    def test_delete_edge(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(3, 2, 6)
        g.delete_edge([1,2])
        self.assertEqual(g.can_reach(2), [3])
        self.assertEqual(g.can_reach(1), [])
        self.assertEqual(g.can_reach(3), [])

    def test_delete_repeated_edge(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(3, 2, 6)
        g.delete_edge([1,2])
        with self.assertRaises(_GraphProperty):
            g.delete_edge([1,2])

    def test_delete_node(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(3, 2, 6)
        g.delete_vertex(2)
        self.assertEqual(g.can_reach(1), [])
        self.assertEqual(g.can_reach(3), [])
        self.assertEqual(g.list_vertices(), [1, 3])

    def test_delete_repeated_node(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2, 5)
        g.add_edge(3, 2, 6)
        g.delete_vertex(2)
        with self.assertRaises(_GraphProperty):
            g.delete_vertex(2)
