from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev1, prev2 = 0,0

        for m in nums:
            curr = max(prev1, prev2 + m)
            prev2 = prev1
            prev1 = curr
        return prev1
        