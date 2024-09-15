from typing import List


class Solution:
    def reverse(self,nums: List[int], start, end):
        i , j = start, end

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:

        self.reverse(nums, 0, len(nums)-1)
        k = k % len(nums)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k, len(nums)-1)

        
        """
        Do not return anything, modify nums in-place instead.
        """
        