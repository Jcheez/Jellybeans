'''
TO DEVELOPERS: DO NOT USE THESE FUNCTION WITHOUT UNDERSTANDING ITS FULL FUNCTIONALITY.
'''
from typing import Any, Callable

def merge(lst:list, start:int, mid:int, end:int, key:Callable) -> None:
    '''
    Description:
        Underlying method two merge 2 lists based on a key
    Args:
        lst: List of elements to be merged
        start: Starting index of the first list to be merged
        mid: Stopping index of the first list to be merged (inclusive)
        end: Stopping index of the second list to be merged
        key: Sorting key
    '''
    temp = []
    left = start
    right = mid+1
    while left <= mid and right <= end:
        if key(lst[left]) <= key(lst[right]):
            temp.append(lst[left])
            left += 1
        else:
            temp.append(lst[right])
            right += 1

    while left <= mid:
        temp.append(lst[left])
        left += 1

    while right <= end:
        temp.append(lst[right])
        right += 1
    for i in range(len(temp)):
        lst[start + i] = temp[i]

def partition(lst:list, start:int, end:int, key:callable) -> int:
    '''
    Description:
        This function seperates elements into 2 different groups.
    Args:
        lst: List of elements to be partitioned
        start: Starting index of elements to partition
        end: Stopping index of elements to partition
        key: Sorting key
    Returns:
        The index of the reference element used to partition the elements
    '''
    pivot = lst[start]
    margin = start
    for idx in range(start+1, end+1):
        if key(lst[idx]) < key(pivot):
            margin += 1
            lst[idx], lst[margin] = lst[margin], lst[idx]
            # swap(lst, idx, margin)
    lst[start], lst[margin] = lst[margin], lst[start]
    #swap(lst, start, margin)
    return margin