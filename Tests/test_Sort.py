import unittest

from Jellybeans.Algos.sorts.Sort import *

class test_sort(unittest.TestCase):
    '''
    Unit tests for sorting algorithms
    '''
    lst_random = [9, 19, 1, 17, 6, 20, 4, 13, 15, 3]
    lst_random_actual = sorted(lst_random.copy())

    lst_random_str = ["ABC", "abc", "adc", "ADC", "98", "7"]
    lst_random_str_actual = sorted(lst_random_str.copy())

    ############################################
    # Testing every sort on a list of integers #
    ############################################
    def test_unsortedList_bubble(self):
        lst = self.lst_random.copy()
        [i for i in bubbleSort(lst)]
        self.assertEqual(lst, self.lst_random_actual)

    def test_unsortedList_bubbleOptimised(self):
        lst = self.lst_random.copy()
        [i for i in bubbleSort_optimised(lst)]
        self.assertEqual(lst, self.lst_random_actual)

    def test_unsortedList_selection(self):
        lst = self.lst_random.copy()
        [i for i in selectionSort(lst)]
        self.assertEqual(lst, self.lst_random_actual)

    def test_unsortedList_insertion(self):
        lst = self.lst_random.copy()
        [i for i in insertionSort(lst)]
        self.assertEqual(lst, self.lst_random_actual)

    def test_unsortedList_merge(self):
        lst = self.lst_random.copy()
        mergeSort(lst)
        self.assertEqual(lst, self.lst_random_actual)

    def test_unsortedList_quick(self):
        lst = self.lst_random_str.copy()
        quickSort(lst)
        self.assertEqual(lst, self.lst_random_str_actual)

    ###########################################
    # Testing every sort on a list of strings #
    ###########################################
    def test_unsortedList_str_bubble(self):
        lst = self.lst_random_str.copy()
        [i for i in bubbleSort(lst)]
        self.assertEqual(lst, self.lst_random_str_actual)

    def test_unsortedList_str_bubbleOptimised(self):
        lst = self.lst_random_str.copy()
        [i for i in bubbleSort_optimised(lst)]
        self.assertEqual(lst, self.lst_random_str_actual)

    def test_unsortedList_str_selection(self):
        lst = self.lst_random_str.copy()
        [i for i in selectionSort(lst)]
        self.assertEqual(lst, self.lst_random_str_actual)

    def test_unsortedList_str_insertion(self):
        lst = self.lst_random_str.copy()
        [i for i in insertionSort(lst)]
        self.assertEqual(lst, self.lst_random_str_actual)

    def test_unsortedList_str_merge(self):
        lst = self.lst_random_str.copy()
        mergeSort(lst)
        self.assertEqual(lst, self.lst_random_str_actual)

    def test_unsortedList_str_quick(self):
        lst = self.lst_random_str.copy()
        quickSort(lst)
        self.assertEqual(lst, self.lst_random_str_actual)