from typing import List


class Solution:
    def sumRange(self,prefix_sum, left: int, right: int) -> int:
        return prefix_sum[right+1] - prefix_sum[left]

    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(len(nums)):
            left_sum = self.sumRange(prefix_sum, 0, i-1) if i > 0 else 0
            right_sum = self.sumRange(prefix_sum, i+1, len(nums)-1) if i < len(nums)-1 else 0
            if left_sum == right_sum:
                return i
        return -1
        
