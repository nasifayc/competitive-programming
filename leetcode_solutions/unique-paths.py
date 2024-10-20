class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = [[0] * n for _ in range(m)]

        def memo(row,col):
            if row == m or col == n:
                return 0
            if c[row][col] > 0:
                return c[row][col]
            if row == m-1 and col == n-1:
                return 1
            c[row][col] = memo(row+1,col) + memo(row,col+1)
            return c[row][col]

        return memo(0,0)