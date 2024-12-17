class Solution:
    def __init__(self, nums):
        self.prefsum = []
        total = 0
        for num in nums:
            total += num
            self.prefsum.append(total)
    def range_sum(self, left, right):
        rightSum = self.prefsum[right]
        leftSum = self.prefsum[left - 1] if left > 0 else 0
        return rightSum - leftSum
    
    

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    obj = Solution(nums)
    print(obj.range_sum(1, 3))  # Output: 9
    print(obj.range_sum(2, 4))  # Output: 12