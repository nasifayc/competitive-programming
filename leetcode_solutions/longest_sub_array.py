from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r,zeros, result, n = 0,0,0,0, len(nums)

        while r < n:
            if nums[r] == 0:
                zeros += 1
            while zeros > 1 and l < r:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            result = max(result, r - l)
            r += 1

        return result if result > 0 else 0