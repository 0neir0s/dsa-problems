from math import inf
from bisect import bisect_left
from functools import cache

def LIS(arr):
    """ Time: O(NlogN)
        Space: O(N) """

    tailTable = [inf]
    for elem in arr:
        if elem < tailTable[0]:
            tailTable[0] = elem
        elif elem > tailTable[-1]:
            tailTable.append(elem)
        else:
            tailTable[bisect_left(tailTable, elem)] = elem
    return len(tailTable)

def LIS_mem(arr):
    """ Time: O(n^2)
        Space: O(N) """

    @cache
    def LISTill(index):
        if index == 0:
            return 1
        return 1 + max(LISTill(j) for j in range(i) if arr[index] > arr[j])
    
    N = len(arr)
    return max((LISTill(index) for index in range(len(arr))), default=0)

def LIS_DP(arr):
    """ Time: O(N^2)
        Space: O(N) """

    matrix = [1]*len(arr)
    for i,elem in enumerate(elem[1:], 1):
        matrix[i] = 1 + max(matrix[j] for j in range(i) if elem > arr[j])

    return matrix[-1]
