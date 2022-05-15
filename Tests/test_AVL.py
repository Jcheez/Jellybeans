import unittest
from Jellybeans.Structures import AVL


class test_AVL(unittest.TestCase):

    def test_insert_normal(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        self.assertEqual(avl.pre_order(), [10, 5, 1, 7, 40, 50])
        self.assertEqual(avl.in_order(), [1, 5, 7, 10, 40, 50])

    def test_insert_rebalance1(self):
        avl = AVL()
        avl.insert(2)
        avl.insert(4)
        avl.insert(3)
        self.assertEqual(avl.pre_order(), [3, 2, 4])

    def test_insert_rebalance2(self):
        avl = AVL()
        avl.insert(1)
        avl.insert(2)
        avl.insert(3)
        self.assertEqual(avl.pre_order(), [2, 1, 3])

    def test_insert_rebalance3(self):
        avl = AVL()
        avl.insert(4)
        avl.insert(2)
        avl.insert(3)
        self.assertEqual(avl.pre_order(), [3, 2, 4])

    def test_insert_rebalance4(self):
        avl = AVL()
        avl.insert(3)
        avl.insert(2)
        avl.insert(1)
        self.assertEqual(avl.pre_order(), [2, 1, 3])

    def test_search(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        self.assertEqual(avl.search(40), 40)
        self.assertEqual(avl.search(41), None)

    def test_delete_normal(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        avl.delete(40)
        avl.delete(1)
        self.assertEqual(avl.pre_order(), [10, 5, 7, 50])
        self.assertEqual(avl.in_order(), [5, 7, 10, 50])

    def test_delete_rebalance1(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        avl.delete(50)
        avl.delete(40)
        self.assertEqual(avl.pre_order(), [5, 1, 10, 7])

    def test_insert_rebalance2(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        avl.delete(50)
        avl.delete(40)
        avl.delete(1)
        self.assertEqual(avl.pre_order(), [7, 5, 10])

    def test_insert_rebalance3(self):
        avl = AVL()
        avl.insert(7)
        avl.insert(5)
        avl.insert(10)
        avl.insert(3)
        avl.delete(10)
        self.assertEqual(avl.pre_order(), [5, 3, 7])

    def test_insert_rebalance4(self):
        avl = AVL()
        avl.insert(5)
        avl.insert(3)
        avl.insert(7)
        avl.insert(20)
        avl.delete(3)
        self.assertEqual(avl.pre_order(), [7, 5, 20])

    def test_insert_min(self):
        avl = AVL()
        avl.insert(5)
        avl.insert(3)
        avl.insert(7)
        avl.insert(20)
        avl.delete(3)
        self.assertEqual(avl.min(), 5)

    def test_insert_max(self):
        avl = AVL()
        avl.insert(5)
        avl.insert(3)
        avl.insert(7)
        avl.insert(20)
        avl.delete(3)
        self.assertEqual(avl.max(), 20)

    def test_insert_successor(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        self.assertEqual(avl.successor(40), 50)
        self.assertEqual(avl.successor(50), None)

    def test_insert_predecessor(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        self.assertEqual(avl.predecessor(1), None)
        self.assertEqual(avl.predecessor(7), 5)

    def test_insert_rank(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        self.assertEqual(avl.rank(5), 2)
        self.assertEqual(avl.rank(50), 6)
        self.assertEqual(avl.rank(3), -1)
        self.assertEqual(avl.rank(1), 1)

    def test_insert_select(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        self.assertEqual(avl.select(5), 40)
        self.assertEqual(avl.select(50), None)
        self.assertEqual(avl.select(3), 7)
        self.assertEqual(avl.select(1), 1)

    def test_insert_orders(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(40)
        avl.insert(1)
        avl.insert(7)
        avl.insert(50)
        self.assertEqual(avl.in_order(), [1, 5, 7, 10, 40, 50])
        self.assertEqual(avl.pre_order(), [10, 5, 1, 7, 40, 50])
        self.assertEqual(avl.post_order(), [1, 7, 5, 50, 40, 10])
