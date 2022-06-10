'''
List of sorting algorithms implemented:
    1. Bubble Sort (Normal / Optimised)
    2. Selection Sort
    3. Insertion Sort
    4. Merge Sort
    5. Quick Sort
    6. Radix Sort
'''
from typing import Callable, Generator
from .private_funcs import swap, merge, partition

def bubble_sort(lst:list, key:Callable = lambda x:x, visualise:bool = False, animate:bool = False) -> Generator:
    '''
    Bubble sort is in place & stable

    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    yield lst.copy()
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if key(lst[j]) > key(lst[j+1]):
                swap(lst, j, j+1)
                if animate:
                    yield lst.copy()

        if visualise:
            yield lst.copy()
        
def bubble_sort_optimised(lst:list, key:Callable = lambda x:x, visualise:bool = False, animate:bool = False) -> Generator:
    '''
    Optimised Bubble sort terminates when there are no swaps happening between elements

    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    yield lst.copy()
    for i in range(len(lst) - 1):
        no_swaps = True
        for j in range(len(lst) - 1):
            if key(lst[j]) > key(lst[j+1]):
                swap(lst, j, j+1)
                no_swaps = False
                if animate:
                    yield lst.copy()

        if visualise:
            yield lst.copy()

        if no_swaps:
            return

def selection_sort(lst:list, key:Callable = lambda x:x, visualise:bool = False, animate:bool = False) -> Generator:
    '''
    Selection sort is in place & not stable

    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    yield lst.copy()
    for i in range(len(lst)-1, 0, -1):
        largest = i
        for j in range(i):
            if key(lst[j]) > key(lst[largest]):
                largest = j
        swap(lst, i, largest)
        if animate or visualise:
            yield lst.copy()

def insertion_sort(lst:list, key:Callable = lambda x:x, visualise:bool = False, animate:bool = False) -> Generator:
    '''
    Insertion sort is in place & stable

    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    yield lst.copy()
    for idx in range(1, len(lst)):
        next = lst[idx]
        j = idx - 1
        while j >= 0 and key(lst[j]) > key(next):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = next
        if animate or visualise:
            yield lst.copy()

def merge_sort(lst:list, key:Callable = lambda x:x, visualise:bool = False, animate:bool = False) -> list:
    '''
    merge sort is not in place & stable

    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    gen = __merge_sort_helper(lst, 0, len(lst)-1, [lst.copy()], key)
    if visualise or animate:
        return gen
    return []

def __merge_sort_helper(lst:list, start:int, end:int, steps:list, key:Callable = lambda x:x) -> list:
    '''
    Merge sort recursive helper function. Divide and conquer method

    Args: 
        lst: Takes in a list 
        start: starting index to sort
        end: last index to sort
        steps: A list of state changes
        key: custom sorting key
    '''
    if (start < end):
        __merge_sort_helper(lst, start, (start + end)//2, steps, key)
        __merge_sort_helper(lst, 1+(start + end)//2, end, steps, key)
        merge(lst, start, (start + end)//2, end, key)
        steps.append(lst.copy())
    return steps

def quick_sort(lst:list, key:Callable = lambda x:x, visualise:bool = False, animate:bool = False) -> list:
    '''
    Quick sort is in place & not stable

    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    gen = __quick_sort_helper(lst, 0, len(lst)-1, [lst.copy()], key)
    if visualise or animate:
        return gen
    return []

def __quick_sort_helper(lst:list, start:int, end:int, steps:list, key:Callable = lambda x:x):
    '''
    Quick sort recursive helper function
    
    Args: 
        lst: Takes in a list 
        start: starting index to sort
        end: last index to sort
        steps: A list of state changes
        key: custom sorting key
    '''
    if (start < end):
        pivot = partition(lst, start, end, key)
        steps.append(lst.copy())
        __quick_sort_helper(lst, start, pivot-1, steps, key)
        __quick_sort_helper(lst, pivot+1, end, steps, key)
    return steps