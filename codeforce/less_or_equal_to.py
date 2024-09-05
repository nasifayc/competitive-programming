from typing import List

class Solution:
    def sortArray(self, nums: List[int], n: int, k: int) -> int:
        
        nums.sort()

        if k == 0:
            
            if nums[0] > 1:
                return 1
            else:
                return -1
        else:
            
            if k == n or nums[k - 1] < nums[k]:
                return nums[k - 1]
            else:
                return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 7, 5, 1, 10, 3, 20]
    n = len(nums)
    k = 2
    print(solution.sortArray(nums, n, k))  
