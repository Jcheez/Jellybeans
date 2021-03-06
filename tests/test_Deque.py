import unittest
from jellybeans.structures import Deque

class test_Queue(unittest.TestCase):

    def test_enqueueFront(self):
        s = Deque()
        self.assertTrue(s.is_empty())
        s.enqueue(1)
        s.enqueue(10)
        s.enqueue_front(5)
        s.enqueue(13)
        s.enqueue(12)
        self.assertFalse(s.is_empty())
        s.dequeue()
        s.dequeue()
        self.assertEqual(s.peek(), 10)
        self.assertEqual(len(s), 3)