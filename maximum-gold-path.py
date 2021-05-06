"""
Leetcode:

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i,j, visited):
            """ returns the maximum gold assuming the path starts at i,j """
            visited.add((i,j))
            output = grid[i][j] + max(
                dfs(i,j+1,visited) if (j+1<N) and ((i,j+1) not in visited ) and grid[i][j+1] else 0,
                dfs(i,j-1,visited) if (0<=j-1) and ((i,j-1) not in visited) and grid[i][j-1] else 0,
                dfs(i+1,j,visited) if (i+1<M) and ((i+1,j) not in visited) and grid[i+1][j] else 0,
                dfs(i-1,j,visited) if (0<=i-1) and ((i-1,j) not in visited) and grid[i-1][j] else 0
            )
            visited.remove((i,j))
            return output

        M, N = len(grid), len(grid[0])
        return max(dfs(i,j,set()) for i in range(M) for j in range(N) if grid[i][j])
