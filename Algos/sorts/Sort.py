'''
List of sorting algorithms implemented:
    1. Bubble Sort (Normal / Optimised)
    2. Selection Sort
    3. Insertion Sort
    4. Merge Sort
    5. Quick Sort
    6. Radix Sort
'''
from .pfuncs import swap, merge, partition

def bubbleSort(lst, key=lambda x:x, visualise=False, animate=False):
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
        
def bubbleSort_optimised(lst, key=lambda x:x, visualise=False, animate=False):
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

def selectionSort(lst, key=lambda x:x, visualise=False, animate=False):
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

def insertionSort(lst, key=lambda x:x, visualise=False, animate=False):
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

def mergeSort(lst, key=lambda x:x, visualise=False, animate=False):
    '''
    merge sort is not in place & stable
    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    gen = __mergeSort_helper(lst, 0, len(lst)-1, [lst.copy()], key)
    if visualise or animate:
        return gen
    return []

def __mergeSort_helper(lst, start, end, steps, key=lambda x:x):
    '''
    Merge sort recursive helper function. Divide and conquer method
    Args: 
        lst: Takes in a list 
        start: starting index to sort
        end: last index to sort
        key: custom sorting key
    '''
    if (start < end):
        __mergeSort_helper(lst, start, (start + end)//2, steps, key)
        __mergeSort_helper(lst, 1+(start + end)//2, end, steps, key)
        merge(lst, start, (start + end)//2, end, key)
        steps.append(lst.copy())
    return steps

def quickSort(lst, key=lambda x:x, visualise=False, animate=False):
    '''
    Quick sort is in place & not stable
    Args: 
        lst: Takes in a list 
        key: custom sorting key
        visualise: print lst after every loop
        animate: used for visualising the animation
    '''
    gen = __quickSort_helper(lst, 0, len(lst)-1, [lst.copy()], key)
    if visualise or animate:
        return gen
    return []

def __quickSort_helper(lst, start, end, steps, key=lambda x:x):
    '''
    Quick sort recursive helper function
    Args: 
        lst: Takes in a list 
        start: starting index to sort
        end: last index to sort
        key: custom sorting key
    '''
    if (start < end):
        pivot = partition(lst, start, end, key)
        steps.append(lst.copy())
        __quickSort_helper(lst, start, pivot-1, steps, key)
        __quickSort_helper(lst, pivot+1, end, steps, key)
    return steps