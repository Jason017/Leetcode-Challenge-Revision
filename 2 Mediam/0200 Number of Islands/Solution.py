from typing import List

class Solution:
    # Solution 1: Recursive DFS
    # O(M*N), O(M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans
        