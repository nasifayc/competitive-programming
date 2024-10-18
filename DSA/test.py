# fibonacci

class Solution:
    def __init__(self):
        self.count = 0
    def fib(self, n: int, c) -> int:
        self.count += 1
        if n <= 1:
            return n
        if n in c:
            return c[n]
        c[n] = self.fib(n-1,c) + self.fib(n-2,c)
        return c[n]
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(100,{}))  # Output: 55
    print(solution.count)