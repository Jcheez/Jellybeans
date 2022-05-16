import unittest
from Jellybeans.Structures import PriorityQueue
from Jellybeans.Structures.Heaps.NotOneBasedIndexed import _NotOneBasedIndexed

class test_Queue(unittest.TestCase):

    def test_isEmpty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.isEmpty())
        pq.insert(1)
        self.assertFalse(pq.isEmpty())
        pq.extract()
        self.assertTrue(pq.isEmpty())

    def test_OneBased(self):
        with self.assertRaises(_NotOneBasedIndexed):
            pq = PriorityQueue(arr=[1,2,3])

    def test_insert1(self):
        pq = PriorityQueue(comparator=lambda x,y:x<=y)
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        self.assertEqual(len(pq), 4)
        self.assertEqual(str(pq), str([None, 6,9,7,10]))

    def test_insert2(self):
        pq = PriorityQueue(arr=[None, 1,30,120,4,5], comparator=lambda x,y:x<=y)
        self.assertEqual(str(pq), str([None, 1, 4, 120, 30, 5]))
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        self.assertEqual(len(pq), 9)
        self.assertEqual(str(pq), str([None, 1, 4, 6, 7, 5, 120, 9, 30, 10]))

    def test_extract1(self):
        pq = PriorityQueue(comparator=lambda x,y:x<=y)
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        pq.extract()
        pq.extract()
        self.assertEqual(len(pq), 2)
        self.assertEqual(str(pq), str([None, 9, 10]))

    def test_extract2(self):
        pq = PriorityQueue(arr=[None, 1,30,120,4,5], comparator=lambda x,y:x<=y)
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        pq.extract()
        pq.extract()
        pq.extract()
        self.assertEqual(len(pq), 6)
        self.assertEqual(str(pq), str([None, 6, 7, 9, 30, 10, 120]))

    def test_peek1(self):
        pq = PriorityQueue(comparator=lambda x,y:x<=y)
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        pq.extract()
        pq.extract()
        self.assertEqual(len(pq), 2)
        self.assertEqual(pq.peek(), 9)

    def test_peek2(self):
        pq = PriorityQueue(arr=[None, 1,30,120,4,5], comparator=lambda x,y:x<=y)
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        pq.extract()
        pq.extract()
        pq.extract()
        self.assertEqual(len(pq), 6)
        self.assertEqual(pq.peek(), 6)

    def test_sort1(self):
        pq = PriorityQueue(comparator=lambda x,y:x<=y)
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        pq.extract()
        pq.extract()
        self.assertEqual(len(pq), 2)
        self.assertEqual(pq.sort(), [9, 10])

    def test_sort2(self):
        pq = PriorityQueue(arr=[None, 1,30,120,4,5], comparator=lambda x,y:x<=y)
        pq.insert(9)
        pq.insert(6)
        pq.insert(7)
        pq.insert(10)
        pq.extract()
        pq.extract()
        pq.extract()
        self.assertEqual(len(pq), 6)
        self.assertEqual(pq.sort(), [6, 7, 9, 10, 30, 120])

    def test_random1(self):
        pq = PriorityQueue(comparator=lambda x,y:len(x) >= len(y))
        pq.insert("a")
        pq.insert("ab")
        pq.insert("abc")
        pq.insert("abcd")
        self.assertEqual(len(pq), 4)
        self.assertEqual(pq.peek(), "abcd")

    def test_random2(self):
        pq = PriorityQueue([None, 1,30,120,4,5])
        self.assertEqual(str(pq), str([None, 120, 30, 1, 4, 5]))