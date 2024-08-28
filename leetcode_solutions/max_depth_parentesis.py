class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxdepth = 0
        for i in s:
            if i == '(':
                count += 1
                if count > maxdepth:
                    maxdepth = count
            elif i == ')':
                count -= 1
        
        return maxdepth
