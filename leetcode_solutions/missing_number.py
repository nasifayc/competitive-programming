from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct = nums[i] 
            if correct < len(nums) and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)