from typing import List


class Solution:
    def sumRange(self, prefix_sum, left: int, right: int) -> int:
        return prefix_sum[right + 1] - prefix_sum[left]

    def subarraySum(self, nums: List[int], k: int) -> int:
       
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        result = 0
        
        prefix_count = {0: 1} 
        current_sum = 0

        for num in nums:
            current_sum += num
            
            if (current_sum - k) in prefix_count:
                result += prefix_count[current_sum - k]
            
            if current_sum in prefix_count:
                prefix_count[current_sum] += 1
            else:
                prefix_count[current_sum] = 1

        return result
