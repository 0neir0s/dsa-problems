"""
Leetcode:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i,j):
            """ Gives you the length of the longest increasing path starting from i,j """
            value = matrix[i][j]
            return 1 + max(
            dfs(i,j+1) if (j+1 < N) and (matrix[i][j] < matrix[i][j+1]) else 0,
            dfs(i,j-1) if (0 <= j-1) and (matrix[i][j] < matrix[i][j-1]) else 0,
            dfs(i+1,j) if (i+1 < M) and (matrix[i][j] < matrix[i+1][j]) else 0,
            dfs(i-1,j) if (0 <= i-1) and (matrix[i][j] < matrix[i-1][j]) else 0
            )

        M, N = len(matrix), len(matrix[0])
        return max( dfs(i,j) for i in range(M) for j in range(len(matrix[0])) )
