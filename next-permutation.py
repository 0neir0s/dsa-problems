def nextPermutation(arr):
	""" Find the next greater permutation after arr """
	N, jump = len(arr), 0
	for k in range(N-2,-1,-1):
		if arr[k] < arr[k+1]:
			jump = k
			break
	else:
		return 
	for k in range(N-1, jump, -1):
		if arr[jump] < arr[k]:
			arr[jump], arr[k] = arr[k], arr[jump]
			break
	arr[jump+1:] = arr[jump+1:][::-1]
	return arr

print(nextPermutation([1,3,2]))
print(nextPermutation([2,3,2,2,1]))
print(nextPermutation([3,2,2,2,1]))

# Useful for all permutations, even with duplications

def allPermutations(arr):
    """ Print all permutations """
    arr.sort()
    while True:
        print(arr)
        arr = nextPermutation(arr)
        if not arr:
            break

print(allPermutations([2,3,1,2,2]))
