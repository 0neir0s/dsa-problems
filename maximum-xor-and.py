# Greedy approaches

def maximumXOR(nums):
  """ Greedy: maximum XOR of two numbers in an array """
  answer = 0
  for i in range(31,-1,-1):
    solSet = {num>>i for num in nums}
    answer, candidate = answer<<1, (answer<<1)+1
    for sol in solSet:
      if sol^candidate in solSet:
        answer = candidate
        break
  return answer

def maximumAND(nums):
  """ Greedy: maximum AND of two numbers in an array """
  answer = 0
  for i in range(31,-1,-1):
    solSet = [ num>>i for num in nums ]
    answer, candidate = answer<<1, (answer<<1)+1
    if sum(sol&candidate == candidate for sol in solSet) > 1:
      answer = candidate
  return answer
