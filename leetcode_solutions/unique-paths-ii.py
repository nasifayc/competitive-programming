from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[row-1][col-1] == 1:
            return 0
        
        dp = [[-1] * col for _ in range(row)]

        def memo(r,c):
            if r == row  or c == col or obstacleGrid[r][c] == 1:
                return 0
            if r == row - 1 and c == col - 1:
                return 1

            if dp[r][c] != -1:
                return dp[r][c]
            
            dp[r][c] = memo(r+1,c) + memo(r,c+1)
            return dp[r][c]

        return memo(0,0)