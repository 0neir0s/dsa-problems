from functools import cache

def subsetSum(elems, total):
    """ Given a set of values and total, check if sum is possible """
    @cache
    def subsetSumWith(index, ssTotal):
        """ check with total can be made with source """
        if ssTotal < 0:
            return False
        if ssTotal == 0:
            return True
        if index == N:
            return False
        value = elems[index]
        subset.add(value)
        if subsetSumWith(index+1, ssTotal-value):
            return True
        subset.remove(value)
        if subsetSumWith(index+1, ssTotal):
            return True

    N, subset = len(elems), set()
    subsetSumWith(0, total)
    return subset
    
# print(subsetSum([3,34,4,5], 9))

# What if it is a map of denominations to no of coins available

DENOMINATION_MAP = {10:5,5:2,2:1}

def limitedMakeChange(denomCol, total):
    """ given collection of coin and total change needed, return if it is possible """
    @cache
    def limMakeChangeFrom(total, denom):
        """ make change with the given highest denominator """
        if denom == 1:
            if total <= denomCol[1]:
                subset.append((total,1))
                return True
            return False
        nextDenom = DENOMINATION_MAP[denom]
        for i in range(0, min(total,denom*denomCol[denom])+1, denom):
            subset.append((i,denom))
            if limMakeChangeFrom(total - i, nextDenom):
                return True
            subset.pop()
        return False
    subset = []
    return limMakeChangeFrom(total, 10), subset

#print(limitedMakeChange({10:1, 5:3, 2:1, 1:1}, 17))



# Generalisation: Knapsack problem
# we are given n items with weight Wi and value Vi, along with a maximum weight capacity of a knapsack W. What's the best way to fit the items into the knapsack to maximize value?

def knapsack(weights, values, W):
    """ Given weights and values, return the maximum value under the weight limit """
    @cache
    def knapsackFrom(index, maxWeight):
        """ return the max value from given index """
        if index == N or maxWeight == 0:
            return 0
        value, weight = values[index], weights[index]
        if weight > maxWeight:
            return knapsackFrom(index+1, maxWeight)
        included = value+knapsackFrom(index+1,maxWeight-weight)
        excluded = knapsackFrom(index+1, maxWeight)
        if included > excluded:
            sack.add(value)
            return included
        return excluded

    N = len(weights)
    sack = set()
    return knapsackFrom(0, W), sack

print(knapsack([10,20,30], [60,100,120], 50))
