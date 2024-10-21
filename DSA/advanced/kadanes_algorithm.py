from typing import List

# max subarray sum
def kadanes(nums: List[int])->int:
    maxSum, curSum = nums[0], 0
    
    for n in nums:
        curSum = max(curSum,0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

n = [4,-1,2,-7,3,4]

print(kadanes(n)) #7