import unittest
from Jellybeans.Structures import TailedLinkedList

class test_TailedLinkedList(unittest.TestCase):
    
    def test_addFront_1(self):
        # Tests if addFront works with a empty LL
        LL = TailedLinkedList()
        LL.addFront(12)
        self.assertEqual(len(LL), 1)
        self.assertEqual(LL.to_list(), [12])
        self.assertEqual(LL.get(0), 12)

    def test_addFront_2(self):
        # Tests if addFront works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.addFront(12)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [12, 9, 7, 4, 3])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_addBack_1(self):
        # Tests if addBack works with a empty LL
        LL = TailedLinkedList()
        LL.addBack(12)
        self.assertEqual(len(LL), 1)
        self.assertEqual(LL.to_list(), [12])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 12)

    def test_addBack_2(self):
        # Tests if addBack works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.addBack(12)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [9, 7, 4, 3, 12])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 12)

    def test_addAtIndex_1(self):
        # Tests if addAtIndex works with an empty LL
        LL = TailedLinkedList()
        LL.addAtIndex(12, 0)
        self.assertEqual(len(LL), 1)
        self.assertEqual(LL.to_list(), [12])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 12)

    def test_addAtIndex_2(self):
        # Tests if addAtIndex works with a LL with 1 element
        LL = TailedLinkedList(12)
        LL.addAtIndex(24, 1)
        self.assertEqual(len(LL), 2)
        self.assertEqual(LL.to_list(), [12, 24])
        self.assertEqual(LL.get(0), 12)
        self.assertEqual(LL.get(len(LL) - 1), 24)

    def test_addAtIndex_3(self):
        # Tests if addAtIndex works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.addAtIndex(12, 3)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [9, 7, 4, 12, 3])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_addAtIndex_4(self):
        # Tests if errors arise when index are erroneous
        LL = TailedLinkedList([9,7,4,3])
        with self.assertRaises(IndexError):
            LL.addAtIndex(12, 5)
        with self.assertRaises(IndexError):
            LL.addAtIndex(12, -5)


    def test_removeFront_1(self):
        # Tests if removeFront works with LL size 1
        LL = TailedLinkedList(13)
        LL.removeFront()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)
        self.assertEqual(LL.get(len(LL) - 1), None)
        self.assertEqual(LL.get(0), None)

    def test_removeFront_2(self):
        # Tests if removeFront works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.removeFront()
        self.assertEqual(len(LL), 3)
        self.assertEqual(LL.to_list(), [7, 4, 3])
        self.assertEqual(LL.get(0), 7)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_removeFront_3(self):
        # Tests if removeFront works with LL size 0
        LL = TailedLinkedList()
        LL.removeFront()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)

    def test_removeBack_1(self):
        # Tests if removeBack works with LL size 0
        LL = TailedLinkedList()
        LL.removeBack()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)

    def test_removeBack_2(self):
        # Tests if removeBack works with a LL size 1
        LL = TailedLinkedList(9)
        LL.removeBack()
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)

    def test_removeBack_3(self):
        # Tests if removeBack works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.addBack(12)
        self.assertEqual(len(LL), 5)
        self.assertEqual(LL.to_list(), [9, 7, 4, 3, 12])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 12)

        
    def test_removeAtIndex_1(self):
        # Tests if removeAtIndex works with a LL with 1 element
        LL = TailedLinkedList(12)
        LL.removeAtIndex(0)
        self.assertEqual(len(LL), 0)
        self.assertEqual(LL.to_list(), [])
        self.assertEqual(LL.get(0), None)
        self.assertEqual(LL.get(len(LL) - 1), None)

    def test_removeAtIndex_2(self):
        # Tests if removeAtIndex works with a non-empty LL
        LL = TailedLinkedList([9,7,4,3])
        LL.removeAtIndex(2)
        self.assertEqual(len(LL), 3)
        self.assertEqual(LL.to_list(), [9, 7, 3])
        self.assertEqual(LL.get(0), 9)
        self.assertEqual(LL.get(len(LL) - 1), 3)

    def test_removeAtIndex_3(self):
        # Tests if errors arise when index are erroneous
        LL = TailedLinkedList([9,7,4,3])
        with self.assertRaises(IndexError):
            LL.removeAtIndex(4)
        with self.assertRaises(IndexError):
            LL.removeAtIndex(-1)

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
        LL.removeAtIndex(1).removeFront().removeBack().addAtIndex(123, 1)
        self.assertEqual(LL.to_list(), [4, 123])
        LL.addBack(234)
        self.assertEqual(LL.get(2), 234)
        self.assertEqual(LL.get(len(LL) - 1), 234)