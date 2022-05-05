import unittest
from Jellybeans.Structures import Stack

class test_Stack(unittest.TestCase):

    def test_isEmpty(self):
        s = Stack()
        self.assertTrue(s.isEmpty())
        s.push(1)
        self.assertFalse(s.isEmpty())
        s.pop()
        self.assertTrue(s.isEmpty())

    def test_peek(self):
        s = Stack()
        self.assertEqual(s.peek(), None)
        s.push(1)
        s.push(3)
        s.push(19)
        self.assertEqual(s.peek(), 19)

    def test_pop(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
        s.push(1)
        s.push(3)
        s.push(19)
        self.assertEqual(s.pop(), 19)
        self.assertEqual(len(s), 2)

    def test_push(self):
        s = Stack()
        s.push(1)
        self.assertEqual(len(s), 1)
        s.push(3)
        self.assertEqual(len(s), 2)
        s.push(19)
        self.assertEqual(len(s), 3)