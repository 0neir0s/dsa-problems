from math import inf

def nextElement(arr, right=True, greater=True):
    """ return the array of next smaller/bigger element to the left/right """
    N = len(arr)
    iterable = range(N-1,-1,-1) if right else range(0,N,1)
    checker = (lambda a,b: a <= b) if greater else (lambda a,b: a >= b)
    output, stack = [-1]*N, []
    for i in iterable:
        val = arr[i]
        while stack and checker(stack[-1],val):
            stack.pop()
        if stack:
            output[i] = stack[-1]
        stack.append(val)
    return output

print(nextElement([2,4,7,1,5], right=True))

def peakElementsV1(arr):
    """ return the peak elements in an array """
    N = len(arr)
    return [elem for i, elem in enumerate(arr) if arr[max(i-1,0)] <= elem <= arr[min(i+1, N-1)]]

print(peakElementsV1([2,2,2,2]))

def findPeakElement(self, nums):
    """ peak element in an array """
    def findPeakElementBetween(start, end):
        if start > end:
            return
        if start == end:
            return start
        mid = (start+end)//2
        val, prev, nxt = nums[mid], nums[mid-1] if mid-1>=0 else -inf, nums[mid+1] if mid+1<N else -inf
        if prev < val > nxt:
            return mid
        elif prev > val:
            return findPeakElementBetween(start, mid-1)
        else:
            return findPeakElementBetween(mid+1, end)

    N = len(nums)
    return findPeakElementBetween(0,N-1)

def findPeekElementMatrix(matrix):
    """ peak element in a matrix """
    def findPeekElementsBetween(startCol, endCol):
        if startCol > endCol:
            return
        midCol = (startCol+endCol)//2
        maxIndex = max(range(M), key= lambda i: matrix[i][midCol]) 
        maxValue = matrix[maxIndex][midCol]
        prev, nxt = matrix[maxIndex][midCol-1] if midCol-1>=0 else -inf, matrix[maxIndex][midCol+1] if midCol+1<N else -inf
        if prev < maxValue > nxt:
            return maxIndex, midCol, maxValue
        elif prev > maxValue:
            return findPeekElementsBetween(startCol, midCol-1)
        else:
            return findPeekElementsBetween(midCol+1, endCol)

    M, N = len(matrix), len(matrix[0])
    return findPeekElementsBetween(0, N-1)

arr = [ [ 10, 8, 10, 10 ],
        [ 14, 13, 12, 11 ],
        [ 15, 9, 11, 21 ],
        [ 16, 17, 19, 20 ] ]

print(findPeekElementMatrix(arr))
