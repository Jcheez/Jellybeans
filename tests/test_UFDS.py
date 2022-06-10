import unittest
from jellybeans.structures import UFDS

class test_UFDS(unittest.TestCase):

    def test_find_set(self):
        ufds = UFDS(5)
        ufds.union(1, 2)
        ufds.union(3, 4)
        ufds.union(3, 5)
        self.assertEqual(ufds.find_set(1), 2)
        self.assertEqual(ufds.find_set(2), 2)
        self.assertEqual(ufds.find_set(3), 4)
        self.assertEqual(ufds.find_set(4), 4)
        self.assertEqual(ufds.find_set(5), 4)

    def test_is_same_set(self):
        ufds = UFDS(5)
        ufds.union(1, 2)
        ufds.union(3, 4)
        ufds.union(3, 5)
        self.assertTrue(ufds.is_same_set(1, 2))
        self.assertFalse(ufds.is_same_set(3, 2))
        self.assertFalse(ufds.is_same_set(4, 2))
        self.assertTrue(ufds.is_same_set(4, 4))
        self.assertTrue(ufds.is_same_set(5, 4))

    def test_union(self):
        ufds = UFDS(6)
        ufds.union(1, 2)
        ufds.union(3, 4)
        ufds.union(5, 6)
        ufds.union(1, 3)
        ufds.union(1, 5)
        self.assertEqual(ufds.count_items(1), 6)

    def test_move1(self):
        ufds = UFDS(3)
        ufds.union(1, 2)
        ufds.move(1, 3)
        self.assertEqual(ufds.count_items(1), 2)      
        self.assertEqual(ufds.count_items(2), 1)      
        self.assertEqual(ufds.count_items(3), 2)

    def test_move2(self):
        ufds = UFDS(3)
        ufds.move(1, 3)
        self.assertEqual(ufds.count_items(1), 2)      
        self.assertEqual(ufds.find_set(1), 3)      
        self.assertEqual(ufds.count_items(2), 1)
    
    def test_move3(self):
        ufds = UFDS(3)
        ufds.move(1, 3)
        ufds.union(2, 3)
        self.assertEqual(ufds.count_items(1), 3)      
        self.assertEqual(ufds.find_set(2), 3)      
        self.assertEqual(ufds.count_items(2), 3)

    def test_count(self):
        ufds = UFDS(5)
        ufds.move(1, 3)
        ufds.union(2, 3)
        ufds.move(4, 5)
        self.assertEqual(ufds.count_items(1), 3)     
        self.assertEqual(ufds.count_items(2), 3)     
        self.assertEqual(ufds.count_items(3), 3)     
        self.assertEqual(ufds.count_items(4), 2)     
        self.assertEqual(ufds.count_items(5), 2)