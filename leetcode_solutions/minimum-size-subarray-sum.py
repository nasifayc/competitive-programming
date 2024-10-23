from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j,total, l = 0,0,0, float("inf")

        while j < len(nums):
            total += nums[j]

            while total >= target:
                l = min(l, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1
        return 0 if l == float("inf") else l
        