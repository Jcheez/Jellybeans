import unittest
from Jellybeans.Structures import UFDS

class test_UFDS(unittest.TestCase):

    def test_findSet(self):
        ufds = UFDS(5)
        ufds.union(1, 2)
        ufds.union(3, 4)
        ufds.union(3, 5)
        self.assertEqual(ufds.findSet(1), 2)
        self.assertEqual(ufds.findSet(2), 2)
        self.assertEqual(ufds.findSet(3), 4)
        self.assertEqual(ufds.findSet(4), 4)
        self.assertEqual(ufds.findSet(5), 4)

    def test_isSameSet(self):
        ufds = UFDS(5)
        ufds.union(1, 2)
        ufds.union(3, 4)
        ufds.union(3, 5)
        self.assertTrue(ufds.isSameSet(1, 2))
        self.assertFalse(ufds.isSameSet(3, 2))
        self.assertFalse(ufds.isSameSet(4, 2))
        self.assertTrue(ufds.isSameSet(4, 4))
        self.assertTrue(ufds.isSameSet(5, 4))

    def test_union(self):
        ufds = UFDS(6)
        ufds.union(1, 2)
        ufds.union(3, 4)
        ufds.union(5, 6)
        ufds.union(1, 3)
        ufds.union(1, 5)
        self.assertEqual(ufds.countItems(1), 6)

    def test_move1(self):
        ufds = UFDS(3)
        ufds.union(1, 2)
        ufds.move(1, 3)
        self.assertEqual(ufds.countItems(1), 2)      
        self.assertEqual(ufds.countItems(2), 1)      
        self.assertEqual(ufds.countItems(3), 2)

    def test_move2(self):
        ufds = UFDS(3)
        ufds.move(1, 3)
        self.assertEqual(ufds.countItems(1), 2)      
        self.assertEqual(ufds.findSet(1), 3)      
        self.assertEqual(ufds.countItems(2), 1)
    
    def test_move3(self):
        ufds = UFDS(3)
        ufds.move(1, 3)
        ufds.union(2, 3)
        self.assertEqual(ufds.countItems(1), 3)      
        self.assertEqual(ufds.findSet(2), 3)      
        self.assertEqual(ufds.countItems(2), 3)

    def test_count(self):
        ufds = UFDS(5)
        ufds.move(1, 3)
        ufds.union(2, 3)
        ufds.move(4, 5)
        self.assertEqual(ufds.countItems(1), 3)     
        self.assertEqual(ufds.countItems(2), 3)     
        self.assertEqual(ufds.countItems(3), 3)     
        self.assertEqual(ufds.countItems(4), 2)     
        self.assertEqual(ufds.countItems(5), 2)