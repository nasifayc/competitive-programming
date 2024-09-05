from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) - 1
        total = 0
        
       
        for i in range(len(piles)):
            total += piles[n - 1]
            n -= 2
            if(n <= i):
                break
            
        
        return total
        