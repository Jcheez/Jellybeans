import unittest
from Jellybeans.Structures import Queue

class test_Queue(unittest.TestCase):

    def test_isEmpty(self):
        s = Queue()
        self.assertTrue(s.isEmpty())
        s.enqueue(1)
        self.assertFalse(s.isEmpty())
        s.dequeue()
        self.assertTrue(s.isEmpty())

    def test_peek(self):
        s = Queue()
        self.assertEqual(s.peek(), None)
        s.enqueue(1)
        s.enqueue(3)
        s.enqueue(19)
        self.assertEqual(s.peek(), 1)

    def test_pop(self):
        s = Queue()
        with self.assertRaises(IndexError):
            s.dequeue()
        s.enqueue(1)
        s.enqueue(3)
        s.enqueue(19)
        self.assertEqual(s.dequeue(), 1)
        self.assertEqual(len(s), 2)

    def test_push(self):
        s = Queue()
        s.enqueue(1)
        self.assertEqual(len(s), 1)
        s.enqueue(3)
        self.assertEqual(len(s), 2)
        s.enqueue(19)
        self.assertEqual(len(s), 3)