from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1,n+1):
            c = 0
            j = i
            while j > 0:
                if j & 1 == 1:
                    c += 1
                j = j >> 1
            res.append(c)
        return res

        