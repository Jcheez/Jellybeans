import unittest
from jellybeans.structures import TailedLinkedList

class test_TailedLinkedList(unittest.TestCase):
    
    def test_add_front_1(self):
        # Tests if add_front works with a empty LL
        LL = TailedLinkedList()
        LL.add_front(12)
        self.assertEqual(len(LL), 1)
        self.assertEqual(LL.to_list(), [12])
        self.assertEqual(LL.get(0), 12)

    def test_add_front_2(self):
        # Tests if add_front works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.add_front(12)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [12, 9, 7, 4, 3])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_add_back_1(self):
        # Tests if add_back works with a empty LL
        LL = TailedLinkedList()
        LL.add_back(12)
        self.assertEqual(len(LL), 1)
        self.assertEqual(LL.to_list(), [12])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 12)

    def test_add_back_2(self):
        # Tests if add_back works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.add_back(12)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [9, 7, 4, 3, 12])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 12)

    def test_add_at_index_1(self):
        # Tests if add_at_index works with an empty LL
        LL = TailedLinkedList()
        LL.add_at_index(12, 0)
        self.assertEqual(len(LL), 1)
        self.assertEqual(LL.to_list(), [12])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 12)

    def test_add_at_index_2(self):
        # Tests if add_at_index works with a LL with 1 element
        LL = TailedLinkedList(12)
        LL.add_at_index(24, 1)
        self.assertEqual(len(LL), 2)
        self.assertEqual(LL.to_list(), [12, 24])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 24)

    def test_add_at_index_3(self):
        # Tests if add_at_index works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.add_at_index(12, 3)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [9, 7, 4, 12, 3])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_add_at_index_4(self):
        # Tests if errors arise when index are erroneous
        LL = TailedLinkedList([9,7,4,3])
        with self.assertRaises(IndexError):
            LL.add_at_index(12, 5)
        with self.assertRaises(IndexError):
            LL.add_at_index(12, -5)


    def test_remove_front_1(self):
        # Tests if remove_front works with LL size 1
        LL = TailedLinkedList(13)
        LL.remove_front()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)
        self.assertEqual(LL.get(len(LL) - 1), None)
        self.assertEqual(LL.get(0), None)

    def test_remove_front_2(self):
        # Tests if remove_front works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.remove_front()
        self.assertEqual(len(LL), 3)
        self.assertEqual(LL.to_list(), [7, 4, 3])
        self.assertEqual(LL.get(0), 7)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_remove_front_3(self):
        # Tests if remove_front works with LL size 0
        LL = TailedLinkedList()
        LL.remove_front()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)

    def test_remove_back_1(self):
        # Tests if remove_back works with LL size 0
        LL = TailedLinkedList()
        LL.remove_back()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)

    def test_remove_back_2(self):
        # Tests if remove_back works with a LL size 1
        LL = TailedLinkedList(9)
        LL.remove_back()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)

    def test_remove_back_3(self):
        # Tests if remove_back works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.add_back(12)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [9, 7, 4, 3, 12])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 12)

        
    def test_remove_at_index_1(self):
        # Tests if remove_at_index works with a LL with 1 element
        LL = TailedLinkedList(12)
        LL.remove_at_index(0)
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)
        self.assertEqual(LL.get(len(LL) - 1), None)

    def test_remove_at_index_2(self):
        # Tests if remove_at_index works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.remove_at_index(2)
        self.assertEqual(len(LL), 3)
        self.assertEqual(LL.to_list(), [9, 7, 3])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_remove_at_index_3(self):
        # Tests if errors arise when index are erroneous
        LL = TailedLinkedList([9,7,4,3])
        with self.assertRaises(IndexError):
            LL.remove_at_index(4)
        with self.assertRaises(IndexError):
            LL.remove_at_index(-1)

    def test_update_1(self):
        # Tests if errors arise when index are erroneous
        LL = TailedLinkedList([9,7,4,3])
        with self.assertRaises(IndexError):
            LL.update(4, 12)
        with self.assertRaises(IndexError):
            LL.update(-1, 12)

    def test_update_2(self):
        # Tests if update works correctly
        LL = TailedLinkedList([9,7,4,3])
        LL.update(0,1)
        LL.update(1,2)
        LL.update(2,3)
        LL.update(3,4)
        self.assertEqual(LL.to_list(), [1,2,3,4])

    def test_get_1(self):
        # Tests if get works correctly
        LL = TailedLinkedList([9,7,4,3])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(1), 7)
        self.assertEqual(LL.get(2), 4)
        self.assertEqual(LL.get(3), 3)

    def test_map_1(self):
        # Tests if map works correctly
        LL = TailedLinkedList([9,7,4,3])
        self.assertEqual(LL.map(lambda x: 2*x).to_list(), [18, 14, 8, 6])

    def test_filter_1(self):
        # Tests if filter works correctly
        LL = TailedLinkedList([9,7,4,3])
        self.assertEqual(LL.filter(lambda x: x%3==0).to_list(), [9, 3])

    def test_len_1(self):
        # Tests if length works correctly
        LL = TailedLinkedList([9,7,4,3])
        self.assertEqual(len(LL), 4)

    def test_equality_1(self):
        # Tests if equality works correctly
        LL = TailedLinkedList([9,7,4,3])
        self.assertEqual(LL == LL, True)

    def test_randomOps_1(self):
        # Tests if filter works correctly
        LL = TailedLinkedList([9,7,4,3])
        LL.remove_at_index(1).remove_front().remove_back().add_at_index(123, 1)
        self.assertEqual(LL.to_list(), [4, 123])
        LL.add_back(234)
        self.assertEqual(LL.get(2), 234)
        self.assertEqual(LL.get(len(LL) - 1), 234)