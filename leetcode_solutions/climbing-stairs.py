class Solution:
    def climbStairs(self, n: int) -> int:
        c = {}

        def check(v):
            if v <= 2:
                return v
            if v in c:
                return c[v]
            c[v] = check(v-1) + check(v-2)
            return c[v]
        return check(n)
        