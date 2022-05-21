'''
TO DEVELOPERS: DO NOT USE THESE FUNCTION WITHOUT UNDERSTANDING ITS FULL FUNCTIONALITY.
'''

from typing import Any

def swap(lst, idx1, idx2):
    '''
    Private method which swaps two elements in a list
    '''
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp

def merge(lst, start, mid, end, key):
    '''
    Underlying method two merge 2 lists based on a key
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

def partition(lst, start, end, key):
    pivot = lst[start]
    margin = start
    for idx in range(start+1, end+1):
        if key(lst[idx]) < key(pivot):
            margin += 1
            swap(lst, idx, margin)
    swap(lst, start, margin)
    return margin